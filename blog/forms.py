from django import forms
from blog.models import Comment


class PostCommentsForms(forms.ModelForm):
    # __id = 0
    #
    # def __init__(self, *args, **kwargs):
    #     super(PostCommentsForms, self).__init__(*args, **kwargs)
    #     self.fields['Post'].required = forms.models.ModelChoiceField(initial=self.__id)
    #     print(self.fields['Post'])
    #
    # def id_stter(self, pid):
    #     self.__id = pid

    class Meta:
        fields = "__all__"
        model = Comment
        exclude = ['id', 'Created date', 'Updated_Date', 'Approved']
