from setuptools import setup
import src.model_execution_worker
import oasislmf.utils 

setup(
    name='ERN_MexicoQuake',
    version='1.0.0.0',
    entry_points={
        'console_scripts': [
            'ERN_MexicoQuake_gulcalc=src.model_execution_worker.ERN_MexicoQuake_gulcalc:main'
        ]
    }
)
