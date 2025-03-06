import re

from django.shortcuts import redirect
from django.urls import reverse


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # print("SimpleMiddleware")
        # One-time configuration and initialization.

    def __call__(self, request):
        path = request.path
        """
            1.判断是否登录
            2.判断是否访问
        """
        # 允许后台不登录情况下访问的路径
        url_list = ['/logout/', '/login/', '/login/register/']
        # 判断session 1、index_app    2、not修改密码   3、login_app
        if (re.match('/index/', path) or re.match('pswd_update', path)) and not re.match('sign_code', path):
            # 重定向到登录页
            sign_code = request.GET.get('sign_code', '')
            if 'name' not in request.session:
                return redirect(f'/login/?path={request.path_info}?sign_code={str(sign_code)}')
        open_urls = ['/admin/login/', '/admin/logout/', '/captchaHostQuery']
        if not request.user.is_authenticated and request.path_info not in open_urls and 'sign_code' in request.path_info:
            return redirect('/admin/login/')
        response = self.get_response(request)
        return response
