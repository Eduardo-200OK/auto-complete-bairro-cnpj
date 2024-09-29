import CNPJextrator as ce
import argparse


def main():
    parser = argparse.ArgumentParser(description="CNPJ para bairro")

    parser.add_argument("file_path", type=str, help="Caminho da pasta para o xlsx. Ex: /home/docs/planilha1.xlsx")
    parser.add_argument("output", type=str, help="Caminho de saida. Ex: /home/docs/saida1.xlsx")
    parser.add_argument("column", type=str, help="Posicao da coluna em que se encontra o CNPJ. Ex: 3")

    args = parser.parse_args()

    file_path = args.file_path
    output = args.output
    column = args.column

    cnpj_extrator = ce.CNPJExtrator(file_path=file_path, column=column, output=output)
    cnpj_extrator.execute()

if __name__ == '__main__':
    main()
