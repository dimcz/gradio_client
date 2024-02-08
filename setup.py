import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="gradio_client",
    version="0.6.1",
    author="Abubakar Abid, Ali Abid, Ali Abdalla, Dawood Khan, Ahsen Khaliq, Pete Allen, Freddy Boulton",
    author_email="team@gradio.app",
    description="Python library for easily interacting with trained machine learning models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gradio-app/gradio",
    project_urls={
        "Bug Tracker": "https://github.com/gradio-app/gradio/issues"
    },
    license="Apache License 2.0",
    packages=["gradio_client"],
    include_package_data=True,
    install_requires=[
        "fsspec",
        "httpx",
        "huggingface_hub>=0.13.0",
        "packaging",
        "requests~=2.0",
        "typing_extensions~=4.0",
        "websockets>=10.0,<12.0",
    ]
)