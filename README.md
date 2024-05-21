## Conversor de Bancos Python

Este script em Python tem como objetivo realizar a cópia de um banco de dados MySQL de origem para um banco de dados MySQL de destino.

## Descrição

O script realiza a leitura das tabelas existentes no banco de origem e copia suas estruturas, campos e dados para o banco de destino. Além disso, ele gera um arquivo de log que detalha todo o processo de conversão.

## Funcionalidades

- **Geração de Log**: Durante a execução, o script gera um arquivo de log que documenta cada etapa do processo, facilitando o acompanhamento e a identificação de possíveis problemas.
- **Leitura das Tabelas de Origem**: O script lê todas as tabelas presentes no banco de dados MySQL de origem.
- **Cópia para o Banco de Destino**: Após a leitura, o script copia as tabelas, incluindo seus campos e os dados nelas contidos, para o banco de dados MySQL de destino.

## Como Usar

1. **Configuração do Script**: Antes de executar o script, configure as informações de conexão para os bancos de dados MySQL de origem e destino.
2. **Execução**: Execute o script em um ambiente Python adequado.
3. **Verificação do Log**: Após a execução, verifique o arquivo de log para assegurar que o processo foi concluído com sucesso.

## Requisitos

- Python 3.x
- Bibliotecas adicionais (`mysql-connector-python` e `logging`)

## Exemplo de Uso

```bash
python conversor_base.py

```

## LICENÇA

Este projeto está licenciado sob a [MIT].

