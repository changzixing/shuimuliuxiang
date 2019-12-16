from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.homepage),
    url('^wechat_login$', views.wechat_login),
    url('^wechat_identity$', views.wechat_identity),
    url('^wechat_signin$', views.wechat_signin),
    url('^CCYL_login$', views.CCYL_login),
    url('^logon$', views.logon),
    url('^login$', views.login),
    url('^test$', views.export_excel),
    #url('^testhtml$', views.testhtml),
    url('^create_activity$', views.create_activity),
    url('^get_activity$', views.get_activity),
    url('^join_group$', views.join_group),
    url('^send_message$', views.send_message),
    url('^edit_user$', views.edit_user),
    url('^send_user_info$', views.send_user_info),
    url('^send_activity_info$', views.send_activity_info),
    url('^join_activity$', views.join_activity),
    url('^get_approve_list$', views.get_approve_list),
    url('^send_message$', views.send_message),
    url('^get_message_list$', views.get_message_list),
    url(r'.*\.html$', views.page_render),
    url('^pass$', views.testpass),
]