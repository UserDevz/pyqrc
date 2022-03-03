<h1 text align='center'>PyQRC</h1></br>
<img src='https://img.shields.io/badge/open%20source-%E2%99%A5%EF%B8%8F-green'>
<img src='https://img.shields.io/badge/language-Python-green'>
<img src='https://img.shields.io/badge/bibliotecas-PyQRCode%2Fpng-green'>
<p>Gerador de códigos qr gerados a partir de um link digitado pelo usuário, projeto criado para implementação em algum software que precise de algo desse tipo e dessa funcionalidade</p></br>
<h2 text align='center'>Sobre o código</h2></br>
<b>Para que o projeto funcione, dependemos de duas bibliotecas que auxiliam na criação do qrcode:</b></br>
</br><li>PyQRCode</br>
<li>png</br></br>
<b>Para usar lo:</b></br>
<p>Insira o Link para gerar o qrcode dentro das aspas ' ':</p></br>

    qrcode = PyQRCode.create('link')

<p>Exemplo:</p></br>

    qrcode= PyQRCode.create('https://github.com/UserDevz/pyqrc')

<p>Logo após, digite o nome do arquivo .png que será criado com o código qr:</p></br>

    qrcode.png('nome.png', scale=6)

<p>Exemplo:</p></br>

    qrcode.png('UserDevz.png', scale=6)

<p>Apenas isso e pronto, seu gerador de qrcode está criado😀</p></br>
