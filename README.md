# Rendertron for BT

### Install & Build

Clone:

```bash
git clone -b bt https://github.com/BeautifulTrouble/rendertron
```

Install dependencies:

```bash
cd rendertron
npm install
python3 -m venv venv
```

Build as normal:

```bash
npm run build
```

### Add services

Install systemd unit files:

```bash
DEST=~/.config/systemd/user
mkdir -p $DEST
ln -sf $(pwd)/rendertron.service $DEST
ln -sf $(pwd)/prerendertron.service $DEST
ln -sf $(pwd)/prerendertron.timer $DEST
systemctl --user daemon-reload
```

### Enable services

Ensure user services run at startup:

```bash
sudo loginctl enable-linger $USER
```

Enable the services:

```bash
systemctl --user enable --now rendertron.service
systemctl --user enable --now prerendertron.timer
```

### Web server:

Proxy appropriate traffic to the rendertron process on 0.0.0.0:3000
