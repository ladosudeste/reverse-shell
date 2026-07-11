# Reverse Shell

## Descrição

Este projeto implementa uma **Reverse Shell** em Python com foco em simplicidade e rapidez de utilização. O script estabelece uma conexão de saída para um host remoto utilizando a porta **4444**, permitindo a execução de comandos remotos após a conexão ser estabelecida.

O objetivo é reduzir a configuração necessária para o uso da ferramenta: basta possuir o Python instalado, executar o script e informar o endereço IP do host que receberá a conexão.

---

## Tecnologias Utilizadas

* **Python 3**
* **socket** — Responsável pela comunicação via TCP.
* **subprocess** — Utilizado para executar comandos do sistema operacional.
* **os** — Manipulação de recursos do sistema operacional.

---

## Pré-requisitos

* Python 3 instalado.
* Conectividade de rede entre o cliente e o host de destino.
* Porta **4444/TCP** disponível para comunicação.

---

## Execução

Execute o script utilizando:

```bash
python reverse.py
```

Ao iniciar, o programa solicitará o endereço IP do host remoto.

A conexão será estabelecida utilizando **TCP** na porta **4444**, definida de forma fixa no código.

---

## Funcionamento

1. O script solicita o endereço IP do host remoto.
2. É criado um socket TCP.
3. O cliente estabelece uma conexão de saída para o IP informado na porta **4444**.
4. Após a conexão, comandos recebidos do host remoto são executados localmente por meio do módulo `subprocess`.
5. A saída dos comandos é enviada de volta ao host remoto através da mesma conexão TCP.

---

## Estrutura

```text
reverse.py
```

---

## Observações

* O script utiliza a porta **4444** como padrão e não realiza seleção dinâmica de portas.
* A comunicação é realizada utilizando sockets TCP.
* O projeto foi desenvolvido para fins de estudo, pesquisa e testes em ambientes autorizados.
