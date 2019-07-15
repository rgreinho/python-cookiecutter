from pathlib import Path

from invoke import task

# Defines variables.
TESTDIR = "test-output"
TOPDIR = Path(".").resolve()
VENV = "venv"
autroprefix = f'source {TOPDIR / "venv/bin/activate"}'


@task(default=True)
def venv(c):
    """Setup the developer environment."""
    venv_path = Path(VENV)
    if venv_path.exists():
        return

    c.run(f"python3 -m venv {VENV}")
    with c.prefix(autroprefix):
        c.run("pip install --upgrade pip setuptools yapf cookiecutter==1.6.0")


@task(pre=[venv])
def ci_prep_env(c):
    """Prepare the test environment."""
    test_dir = Path(TESTDIR).resolve()
    test_dir.mkdir(exist_ok=True)
    with c.prefix(autroprefix):
        with c.cd(f"{test_dir}"):
            c.run(f"cookiecutter --no-input --overwrite-if-exists {TOPDIR}")


@task
def clean(c):
    """Remove unwanted files in project (!DESTRUCTIVE!)."""
    c.run("git clean -ffdx")
    c.run("git reset --hard")


@task(pre=[ci_prep_env])
def test(c):
    """Test the cookicutter."""
    project_dir = Path(TESTDIR) / "project"
    with c.cd(f"{project_dir.resolve()}"):
        c.run("inv")
        c.run("nox -s ci")
