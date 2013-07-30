# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Comment.user'
        db.add_column(u'articles_comment', 'user', self.gf('django.db.models.fields.CharField')(default='NULL', max_length=20), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Comment.user'
        db.delete_column(u'articles_comment', 'user')


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
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.CharField', [], {'default': "'NULL'", 'max_length': '20'})
        }
    }

    complete_apps = ['articles']
