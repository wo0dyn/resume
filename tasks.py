from glob import glob
import os

from invoke import ctask as task


BASE = 'Nicolas-Dubois-cv-fr.{ext}'


@task(default=True)
def build(context, open_pdf=True):
    """
    Build PDF from LaTeX sources and open it in the default PDF viewer.
    """
    context.run('pdflatex ' + BASE.format(ext='tex'))
    context.run('pdflatex ' + BASE.format(ext='tex'))
    if open_pdf:
        context.run('open ' + BASE.format(ext='pdf'))


@task
def clean(context):
    """
    Remove non-(La)TeX files (temp files and PDFs).
    """
    for f in set(glob(BASE.format(ext='*'))) - set(glob('*.tex')):
        os.remove(f)
