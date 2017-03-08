# search_indexes.py

from haystack import indexes
from asset.models import Asset


class AssetIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    room = indexes.CharField(model_attr='room')

    def get_model(self):
        return Asset

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()