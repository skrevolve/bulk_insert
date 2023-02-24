# bulk_insert

## install python
>
    # 👇️ in a virtual environment or using Python 2
    $ pip install pyodbc

    # 👇️ for python 3 (could also be pip3.10 depending on your version)
    $ pip3 install pyodbc

    # 👇️ if you get permissions error
    $ sudo pip3 install pyodbc
    $ pip install pyodbc --user

    # 👇️ if you don't have pip in your PATH environment variable
    $ python -m pip install pyodbc

    # 👇️ for python 3 (could also be pip3.10 depending on your version)
    $ python3 -m pip install pyodbc

    # 👇️ using py alias (Windows)
    $ py -m pip install pyodbc

    # 👇️ for Anaconda
    $ conda install -c anaconda pyodbc

    # 👇️ for Jupyter Notebook
    $ !pip install pyodbc

## prepare
>
    $ pip install pyodbc
    $ pip install pandas

## zsh config
>
    # 👇️ search python path
    $ which python3

>
    # 👇️ insert -> alias python="which python3 result path"
    $ vi ~/.zshrc

>
    # 👇️ reset zshrc
    $ source ~/.zshrc

>
    # 👇️ check version
    $ python --version