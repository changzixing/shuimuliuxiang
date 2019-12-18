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
    url('^export_excel$', views.export_excel),
    #url('^testhtml$', views.testhtml),
    url('^create_activity$', views.create_activity),
    url('^get_activity$', views.get_activity),
    url('^add_acc$', views.add_acc),
    url('^group_list$', views.group_list),
    url('^send_group_info$', views.send_group_info),
    url('^edit_group_info$', views.edit_group_info),
    url('^follow_list$', views.follow_list),
    url('^follow_group$', views.follow_group),
    url('^unfollow_group$', views.unfollow_group),
    url('^send_message$', views.send_message),
    url('^edit_user$', views.edit_user),
    url('^send_user_info$', views.send_user_info),
    url('^send_activity_info$', views.send_activity_info),
    url('^join_activity$', views.join_activity),
    url('^get_approve_list$', views.get_approve_list),
    url('^get_manage_list$', views.get_manage_list),
    url('^pass_activity$', views.pass_activity),
    url('^deny_activity$', views.deny_activity),
    url('^manage_one_activity$', views.manage_one_activity),
    url('^send_rank$', views.send_rank),
    url('^send_message$', views.send_message),
    url('^get_message_list$', views.get_message_list),
    url('^get_detail_message$', views.get_detail_message),
    url(r'.*\.html$', views.page_render),
    url('^test$', views.test),

]