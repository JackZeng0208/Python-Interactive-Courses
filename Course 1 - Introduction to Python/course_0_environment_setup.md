# Preparation

- Miniconda (including Python)
- Visual Studio Code
- Other necessary libraries

# Miniconda

- China Mainland: [Index of /anaconda/miniconda/ | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/)
  - Install corresponding version based on your OS
    - MacOS -> xxx-arm64.pkg
    - Windows -> Windows-x86_64.exe
    - Linux -> Linux-x86_64.sh
      - chmod +x your_installation_script.sh
      - ./your_installation_script.sh
- Other: [Installing Miniconda — Anaconda documentation](https://docs.anaconda.com/free/miniconda/miniconda-install/)
  - Follow the docs directly
## Change download channels (if you are in Mainland China)

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/

conda config --set show_channel_urls yes
```
## Visual Studio Code

- China Mainland: http://soft.qq.com/detail/16/detail_22856.html
- Other: [Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/)

## Other necessary libraries

```bash
pip install -r requirements.txt
```
