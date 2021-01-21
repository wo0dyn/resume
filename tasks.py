from glob import glob
import os

from invoke import task


BASE = 'Nicolas-Dubois-cv-fr'


@task(default=True, name='build')
def _build(context):
    """
    Build PDF from LaTeX sources and open it in the default PDF viewer.
    """
    _compile(context)
    _open(context)


@task(name='compile')
def _compile(context, force=False):
    """
    Compile LaTeX sources.
    """
    context.run(f'pdflatex {BASE}.tex')
    context.run(f'bibtex {BASE}')
    context.run(f'pdflatex {BASE}.tex')
    context.run(f'pdflatex {BASE}.tex')


@task(name='open')
def _open(context):
    """
    Open PDF file in default PDF viewer.
    """
    context.run(f'open {BASE}.pdf')


@task(name='clean')
def _clean(context):
    """
    Remove non-(La)TeX files (temp files and PDFs).
    """
    for f in set(glob(f"{BASE}.*")) - set(glob('*.tex')):
        os.remove(f)
