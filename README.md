# 2466-dj5-blog
Membuat Aplikasi Blog Menggunakan Django versi 5.0.4
Github:https://github.com/gurnitha/2466-dj5-blog
Local:E:\_WORKSPACE\2024\django\2466\2466-django-5-by-example


## 1. SETUP


#### 1. Membuat remote repositori 

        modified:   README.md


#### 2. Membuat lingkungan virtual

        E:\_WORKSPACE\2024\django\2466\2466-django-5-by-example\2466-dj5-blog(main -> origin)
        λ python --version
        Python 3.12.1

        E:\_WORKSPACE\2024\django\2466\2466-django-5-by-example\2466-dj5-blog(main -> origin)
        λ pip --version
        pip 24.0 from E:\_WORKSPACE\laragon\bin\python\python-3.12\Lib\site-packages\pip (python 3.12)

        E:\_WORKSPACE\2024\django\2466\2466-django-5-by-example\2466-dj5-blog(main -> origin)
        λ virtualenv --version
        virtualenv 20.26.0 from E:\_WORKSPACE\laragon\bin\python\python-3.12\Lib\site-packages\virtualenv\__init__.py

        E:\_WORKSPACE\2024\django\2466\2466-django-5-by-example\2466-dj5-blog(main -> origin)
        λ python -m venv venv312504 --promp dj5-blog

        E:\_WORKSPACE\2024\django\2466\2466-django-5-by-example\2466-dj5-blog(main -> origin)
        λ ls
        README.md  venv312504/

        modified:   .gitignore
        modified:   README.md


#### 3. Menginstal Django versi 5.0.4

        λ REM: Menginstal Django versi 5.0.4

        E:\_WORKSPACE\2024\django\2466\2466-django-5-by-example\2466-dj5-blog(main -> origin)
        λ venv312504\Scripts\activate.bat

        E:\_WORKSPACE\2024\django\2466\2466-django-5-by-example\2466-dj5-blog(main -> origin)
        (dj5-blog) λ pip install django==5.0.4
        Collecting django==5.0.4
          Obtaining dependency information for django==5.0.4 from https://files.pythonhosted.org/packages/d3/31/32ce7eb77accc1678054fe951228766b47f9ec7d68d96d1caaa2611cbafe/Django-5.0.4-py3-none-any.whl.metadata
          Using cached Django-5.0.4-py3-none-any.whl.metadata (4.1 kB)
        Collecting asgiref<4,>=3.7.0 (from django==5.0.4)
          Obtaining dependency information for asgiref<4,>=3.7.0 from https://files.pythonhosted.org/packages/39/e3/893e8757be2612e6c266d9bb58ad2e3651524b5b40cf56761e985a28b13e/asgiref-3.8.1-py3-none-any.whl.metadata
          Using cached asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
        Collecting sqlparse>=0.3.1 (from django==5.0.4)
          Obtaining dependency information for sqlparse>=0.3.1 from https://files.pythonhosted.org/packages/43/5d/a0fdd88fd486b39ae1fd1a75ff75b4e29a0df96c0304d462fd407b82efe0/sqlparse-0.5.0-py3-none-any.whl.metadata
          Using cached sqlparse-0.5.0-py3-none-any.whl.metadata (3.9 kB)
        Collecting tzdata (from django==5.0.4)
          Obtaining dependency information for tzdata from https://files.pythonhosted.org/packages/65/58/f9c9e6be752e9fcb8b6a0ee9fb87e6e7a1f6bcab2cdc73f02bb7ba91ada0/tzdata-2024.1-py2.py3-none-any.whl.metadata
          Using cached tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)
        Using cached Django-5.0.4-py3-none-any.whl (8.2 MB)
        Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
        Using cached sqlparse-0.5.0-py3-none-any.whl (43 kB)
        Using cached tzdata-2024.1-py2.py3-none-any.whl (345 kB)
        Installing collected packages: tzdata, sqlparse, asgiref, django
        Successfully installed asgiref-3.8.1 django-5.0.4 sqlparse-0.5.0 tzdata-2024.1

        [notice] A new release of pip is available: 23.2.1 -> 24.0
        [notice] To update, run: python.exe -m pip install --upgrade pip


#### 4. Meng-upgrade pip

        (dj5-blog) λ python.exe -m pip install --upgrade pip
        Requirement already satisfied: pip in e:\_workspace\2024\django\2466\2466-django-5-by-example\2466-dj5-blog\venv312504\lib\site-packages (23.2.1)
        Collecting pip
          Obtaining dependency information for pip from https://files.pythonhosted.org/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl.metadata
          Using cached pip-24.0-py3-none-any.whl.metadata (3.6 kB)
        Using cached pip-24.0-py3-none-any.whl (2.1 MB)
        Installing collected packages: pip
          Attempting uninstall: pip
            Found existing installation: pip 23.2.1
            Uninstalling pip-23.2.1:
              Successfully uninstalled pip-23.2.1
        Successfully installed pip-24.0