# pysampleproject

A Python template for development in VSC. Inspired by https://github.com/pypa/sampleproject.

## Create virtual environment

Use the "Python: Create Environment..." task in VSC.

## Dev install in the environment

Install editable:

```shell
pip install --editable .[dev,test]
```

Install editable in strict mode:

```shell
pip install ---editable .[dev,test] --config-settings editable_mode=strict
```

## Testing

Install nox:

```shell
pip install nox
```

Run tests:
```shell
nox -s tests
```

## Install globally the system (Windows)

```shell
pyinstaller sample.spec
```
