import boto3

access_key = 'ASIA2HVQ5TXCZEHGI4SS'
secret_access_key = 'zjWzl5dse3KxLBpStKS99+HPviqa3owHy7I9KTEe'
session_token = 'IQoJb3JpZ2luX2VjEMv//////////wEaCXVzLWVhc3QtMSJHMEUCIE7RTj3HIMv/++RzmXeLMqtM2vlx585OWhi8q73qrPvbAiEA5YuteDMP4PsMlyqjR5Pypa/naWj6WIERmGTmD8+hQJQqqAMIlP//////////ARAAGgw3MDM2NzE5MzQ0MDUiDFQ/8cUt8pqfEPb1Lyr8AtkJkNVY8EJmHLg+0gZPU1rPrcgk+XvACNazvejtDF/+4pxnCgFVboZtkgq4fRHlHYbAa8JOGaYUFkB0Esdjb+pxgbMoLyktc8PEBnir3gEwgYUONLUrglKFpUi8b5Mr1O1gqm+IvTI9SFnilFocDXSr2OdKR6QYmWYeB7pv+8R+PpImcmruulrKhIPoI8fmQbiI2B04KPkC8Rg967dM413xWYPQoq8nI2NgTudYSXHWjGaoN8TzPtwf95NOCmLKDqpyHETAZG82FFL3uBu9gRNyY2g/Eb0AWmI89hht/uMkLNt61Agb2/Vf9W8zOWN1kRlf9TAmooHX2EecGqee1htHDl33SxP4xquy+D6su7e3pQPV+sHylHOGJn+1k0/P0XAgnYB299BG2NrBglj6avhxRUAkeknrSqOtCdd6kHFszOLm3jiDyQ8rK/CV8MqenY5BvGMQGWH5LKcXLgyShCL1d6+oRTuzyav9p4lLx4KJ/dribeKWNeZOCaJqMKvxlrsGOqYBtnKEqYByeZgbG7SjF3zRTeg3qmcTrjvmyLsaijTyxk6kkk1Otg4nOPomBetLxSe1lPvoMFMlK8Dp2KT6V5OdmtxWTGEtVsPChJTw57CM5SIpaBlMggGkqOI/S4p1bsT4HYmgSdKEdCMgbdNOzpL27FM3BqFwOAWM3oOp6C22H15MSdBq3xSE9ll3wCEBxbCl2oeKpk87oRIOPX+AbqA/qHlPkGz/Sw=='

s3 = boto3.resource(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token
)

nome_bucket = "bucket-contratos-capes"
arquivo_local_tratamento = "C:/Users/proge/desafio_compass/Desafio_python/Contratos_Capes_Tratado.csv"
arquivo_local_resultado_final = "C:/Users/proge/desafio_compass/Desafio_python/resultado_filtrado.csv"

try:
    s3.meta.client.upload_file(
        arquivo_local_tratamento, nome_bucket, "Contratos_Capes_Tratado.csv")
    print(f"Arquivo tratado enviado para '{nome_bucket}'")
except Exception as e:
    print(f"Erro ao enviar o arquivo tratado: {e}")

try:
    s3.meta.client.upload_file(
        arquivo_local_resultado_final, nome_bucket, "resultado_filtrado.csv")
    print(f"Resultado final da análise enviado para '{nome_bucket}'")
except Exception as e:
    print(f"Erro ao enviar o arquivo tratado: {e}")
