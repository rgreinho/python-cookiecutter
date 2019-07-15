from pathlib import Path
import os

from invoke import task
from nox.virtualenv import VirtualEnv

# Configuration values.
VENV = 'venv'
project_name = '{{ cookiecutter.project_name }}'
docker_org = '{{ cookiecutter.project_name }}'
docker_repo = f'{docker_org}/{project_name}'


@task
def build_docker(c):
    """Build a docker image."""
    tag = c.run('git describe', hide=True)
    docker_img = f'{docker_repo}:{tag.stdout.strip()}'
    c.run(f'docker build -t {docker_img} .')


@task
def clean(c):
    """Remove unwanted files and artifacts in this project (!DESTRUCTIVE!)."""
    clean_docker(c)
    clean_repo(c)


@task
def clean_docker(c):
    """Remove all docker images built for this project (!DESTRUCTIVE!)."""
    c.run(f'docker image rm -f $(docker image ls --filter reference={docker_repo} -q) || true')


@task
def clean_repo(c):
    """Remove unwanted files in project (!DESTRUCTIVE!)."""
    c.run('git clean -ffdx')
    c.run('git reset --hard')


@task
def dist(c):
    """Package the application."""
    with c.prefix(autoprefix()):
        c.run('python setup.py bdist_wheel')


@task
def dist_upload(c):
    """Upload the packaged application."""
    with c.prefix(autoprefix()):
        c.run('twine upload dist/*')


@task
def flame_graph(c):
    """Create an interactive CPU flame graph profile."""
    _, venv_bin, = get_venv(VENV)
    {{cookiecutter.project_name}} = venv_bin / '{{ cookiecutter.project_name }}'
    with c.prefix(autoprefix()):
        c.run(f'sudo py-spy -d 20 --flame profile.svg -- { {{ cookiecutter.project_name }}.resolve() } -v --pages 5')


@task
def nox(c, s=''):
    """Wrapper for the nox tasks (`inv nox` for details)."""
    if not s:
        c.run('nox --list')
    else:
        c.run(f'nox -s {s}')


@task
def profile(c):
    """Create an interactive CPU flame graph."""
    _, venv_bin, _ = get_venv(VENV)
    with c.prefix(autoprefix()):
        c.run(
            f'pyinstrument --renderer html {(venv_bin /project_name ).resolve()} -v --format count --pages 5',
            pty=True,
        )


@task
def publish(c, cname):
    """Publish the documentation."""
    origin = 'origin' if os.getenv('CIRCLECI') else 'upstream'
    r = c.run('git describe')
    git_sha = r.stdout.rstrip()
    with c.prefix(autoprefix()):
        c.run(f'ghp-import -n -p -f -c {cname} -r "{origin}" -m "Publish {git_sha}" docs/build/html/')


@task(default=True)
def setup(c):
    """Setup the developper environment."""
    c.run('nox --envdir .')


def get_venv(venv):
    """
    Return `Path` objects from the venv.
    :param str venv: venv name
    :return: the venv `Path`, the `bin` folder `Path` within the venv, and if specified, the `Path` object of the
        activate script within the venv.
    :rtype: a tuple of 3 `Path` objects.
    """
    location = Path(venv)
    venv = VirtualEnv(location.resolve())
    venv_bin = Path(venv.bin)
    activate = venv_bin / 'activate'
    return venv, venv_bin, activate


def autoprefix(venv='venv'):
    """[summary]

    :param venv: [description], defaults to 'venv'
    :type venv: str, optional
    """
    _, _, activate = get_venv(venv)
    return f'source {activate.resolve}' if activate.exists() else 'true'
