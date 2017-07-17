from glob import glob
import os

from invoke import task


BASE = 'Nicolas-Dubois-cv-fr.{ext}'


@task(default=True, name='build')
def _build(context):
    """
    Build PDF from LaTeX sources and open it in the default PDF viewer.
    """
    _compile(context)
    _open(context)


@task(name='compile')
def _compile(context):
    """
    Compile LaTeX sources.
    """
    context.run('pdflatex ' + BASE.format(ext='tex'))
    context.run('pdflatex ' + BASE.format(ext='tex'))


@task(name='open')
def _open(context):
    """
    Open PDF file in default PDF viewer.
    """
    context.run('open ' + BASE.format(ext='pdf'))


@task(name='clean')
def _clean(context):
    """
    Remove non-(La)TeX files (temp files and PDFs).
    """
    for f in set(glob(BASE.format(ext='*'))) - set(glob('*.tex')):
        os.remove(f)


@task(name='edit')
def _edit(context):
    """
    Edit LaTeX sources.
    """
    context.run('open ' + BASE.format(ext='tex'))
