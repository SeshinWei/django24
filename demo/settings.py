"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os, sys
# sys.path
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 项目根路由
# /Users/chao/Desktop/demo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# print(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Django自带的密钥,将来如果需要进行加密处理可以用此密钥
SECRET_KEY = 'xx+5r-%#csi71j88j15l-w+v%@&y=yx#mngwm#=3h!o=$-=+va'

# SECURITY WARNING: don't run with debug turned on in production!
# 默认开启调试模式,将来项目部署上线时,需要把DEBUG改为False
# 如果将来项目部署上线后,Django服务器不再提供对静态文件访问的支持, 因为Django服务器是动态业务逻辑服务器,不擅长静态文件处理,将来静态文件访问
# 需要放到nginx静态文件服务器
DEBUG = True

# 允许那个域名访问django项目
ALLOWED_HOSTS = []


# Application definition
# 安装或注册Django自带子应用 及第三方或自己创建的子应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users.apps.UsersConfig',   # 注册子应用
    # 子应用可以注册也可以不注册?
]

# 中间件 类似于flask中的请求勾子
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 工程配置的路由入口文件
ROOT_URLCONF = 'demo.urls'

# 模板文件配置项
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 部署上线后工程启动入口
WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# 数据库配置项
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

# 密码验证配置项
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
# 工程语言 默认是英文 可以修改为简体中心  zh-hans
LANGUAGE_CODE = 'en-us'

# 时区  默认是世界时间 可以修改为亚洲/上海时区  Asia/Shanghai
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# 静态文件访问的路由前缀
STATIC_URL = '/static/'
# http://127.0.0.1:8000/static/index.html
# http://127.0.0.1:8000/static/mm03.jpg
# 配置静态文件加载存储目录
STATICFILES_DIRS = [
    # /Users/chao/Desktop/demo/static_files
    os.path.join(BASE_DIR, 'static_files'),
    os.path.join(BASE_DIR, 'static_files/test'),
]

# redis数据库配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.103.210:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"  # 设置session有内存缓存
SESSION_CACHE_ALIAS = "default"  # 缓存到redis default名的配置redis