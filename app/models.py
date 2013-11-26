import os
import os.path as op

from app import db
from sqlalchemy import event
from wtforms import fields
from werkzeug import secure_filename
from flask import request

from flask.ext.admin.form import RenderTemplateWidget
from flask.ext.admin.model.form import InlineFormAdmin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.contrib.sqla.form import InlineModelConverter
from flask.ext.admin.contrib.sqla.fields import InlineModelFormList

# Figure out base upload path
base_path = op.join(op.dirname(__file__), 'static')


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author = db.Column(db.String(128))
    description = db.Column(db.Text)
    air_date = db.Column(db.Date)
    url = db.Column(db.String(128))

    def __repr__(self):
        return '<Book %r>' % (self.title)


class BookImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.Unicode(128))
    path = db.Column(db.String(64))

    location_id = db.Column(db.Integer, db.ForeignKey(Book.id))
    location = db.relation(Book, backref='images')


# Register after_delete handler which will delete image file after model gets deleted
@event.listens_for(BookImage, 'after_delete')
def _handle_image_delete(mapper, conn, target):
    try:
        if target.path:
            os.remove(op.join(base_path, target.path))
    except:
        pass


# This widget uses custom template for inline field list
class CustomInlineFieldListWidget(RenderTemplateWidget):
    def __init__(self):
        super(CustomInlineFieldListWidget, self).__init__('field_list.html')


# This InlineModelFormList will use our custom widget
class CustomInlineModelFormList(InlineModelFormList):
    widget = CustomInlineFieldListWidget()


# Create custom InlineModelConverter and tell it to use our InlineModelFormList
class CustomInlineModelConverter(InlineModelConverter):
    inline_field_list_type = CustomInlineModelFormList


# Customized inline form handler
class InlineModelForm(InlineFormAdmin):
    form_excluded_columns = ('path',)

    form_label = 'Image'

    def __init__(self):
        return super(InlineModelForm, self).__init__(BookImage)

    def postprocess_form(self, form_class):
        form_class.upload = fields.FileField('Image')
        return form_class

    def on_model_change(self, form, model):
        file_data = request.files.get(form.upload.name)

        if file_data:
            model.path = secure_filename(file_data.filename)
            file_data.save(op.join(base_path, model.path))


# Administrative class
class BookAdmin(ModelView):
    inline_model_form_converter = CustomInlineModelConverter

    inline_models = (InlineModelForm(),)

    def __init__(self):
        super(BookAdmin, self).__init__(Book, db.session, name='Books')
