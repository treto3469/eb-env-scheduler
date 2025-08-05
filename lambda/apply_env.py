import os
import subprocess
import boto3

BUCKET = "tu-bucket-s3"
PREFIX = "terraform/envs/qa"

def lambda_handler(event, context):
    # Cambiar a /tmp
    os.chdir("/tmp")

    # Descargar archivos de S3
    s3 = boto3.client("s3")
    for key in ["main.tf", "variables.tf", "backend.tf"]:
        s3.download_file(BUCKET, f"{PREFIX}/{key}", key)

    # Ejecutar Terraform
    subprocess.run(["terraform", "init"], check=True)
    subprocess.run(["terraform", "apply", "-auto-approve"], check=True)

    return {"status": "Entorno QA encendido con éxito"}
