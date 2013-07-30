# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Comment.pub_date'
        db.add_column(u'articles_comment', 'pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2013, 7, 21), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Comment.pub_date'
        db.delete_column(u'articles_comment', 'pub_date')


    models = {
        u'articles.article': {
            'Meta': {'object_name': 'Article'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'articles.comment': {
            'Meta': {'object_name': 'Comment'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.Article']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'default': "'NULL'", 'max_length': '20'})
        }
    }

    complete_apps = ['articles']
