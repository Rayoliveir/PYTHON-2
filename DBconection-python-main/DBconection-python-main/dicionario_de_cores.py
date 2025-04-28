# Cores de texto
TEXT_COLORS = {
    "preto": "\033[30m",
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "magenta": "\033[35m",
    "ciano": "\033[36m",
    "branco": "\033[37m",
    "cinza": "\033[90m",
    "vermelho claro": "\033[91m",
    "verde claro": "\033[92m",
    "amarelo claro": "\033[93m",
    "azul claro": "\033[94m",
    "magenta claro": "\033[95m",
    "ciano claro": "\033[96m",
    "branco brilhante": "\033[97m",
}

# Cores de fundo
BACKGROUND_COLORS = {
    "preto": "\033[40m",
    "vermelho": "\033[41m",
    "verde": "\033[42m",
    "amarelo": "\033[43m",
    "azul": "\033[44m",
    "magenta": "\033[45m",
    "ciano": "\033[46m",
    "branco": "\033[47m",
    "cinza": "\033[100m",
    "vermelho claro": "\033[101m",
    "verde claro": "\033[102m",
    "amarelo claro": "\033[103m",
    "azul claro": "\033[104m",
    "magenta claro": "\033[105m",
    "ciano claro": "\033[106m",
    "branco brilhante": "\033[107m",
}

RESET = "\033[0m"

# Exemplo de impressão
for color_name, color_code in TEXT_COLORS.items():
    print(f"{color_code}Texto em {color_name}{RESET}")

for bg_color_name, bg_color_code in BACKGROUND_COLORS.items():
    print(f"{bg_color_code}Texto com fundo {bg_color_name}{RESET}")
