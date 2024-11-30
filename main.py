import os

def contar_linhas_pasta(base_dir):
    total_linhas = 0
    for root, dirs, files in os.walk(base_dir):
        # Ignorar pastas específicas
        dirs[:] = [d for d in dirs if d not in ['.dart_tool', '.git', '.idea', 'build', 'ios', 'macos', 'windows', 'linux', 'web', 'android/.gradle']]

        for file in files:
            # Ignorar arquivos específicos e binários
            if file in ['.env', '.flutter-plugins', '.flutter-plugins-dependencies', '.metadata', 'pubspec.lock', 'firebase.json', 'README.md', 'CHANGELOG.md', 'analysis_options.yaml'] or file.endswith(('.png', '.jpg', '.jpeg', '.jar', '.jks', '.bin', '.lock')):
                continue
            file_path = os.path.join(root, file)
            try:
                # Somente tentar abrir arquivos de texto
                with open(file_path, 'r', encoding='utf-8') as f:
                    total_linhas += sum(1 for _ in f)
            except (UnicodeDecodeError, IsADirectoryError, FileNotFoundError):
                # Ignorar erros ao tentar ler arquivos binários ou diretórios
                continue
    return total_linhas

def contar_linhas_microservicos(base_dir):
    print(f"Contando linhas de código no diretório: {base_dir}...")
    total_linhas = contar_linhas_pasta(base_dir)
    print(f"\nTotal de linhas de código criadas no projeto: {total_linhas}")

# Diretório base do front-end
base_dir = input("Informe o diretório base do projeto front-end: ").strip()
contar_linhas_microservicos(base_dir)