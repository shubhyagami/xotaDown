#!/bin/bash

# === Aria2 Installer Script ===
# Works on Debian/Ubuntu systems
# If no sudo, it will still compile and run locally

set -e

echo "🔄 Updating package list..."
sudo apt-get update || true

echo "📦 Installing dependencies..."
sudo apt-get install -y git gcc g++ make autoconf automake autotools-dev autopoint \
    libtool pkg-config libssl-dev libxml2-dev libcppunit-dev libgcrypt-dev \
    libgpg-error-dev libsqlite3-dev zlib1g-dev || true

# === Clone aria2 if not already ===
if [ ! -d "aria2" ]; then
    echo "📥 Cloning aria2 repository..."
    git clone https://github.com/aria2/aria2.git
fi

cd aria2

echo "⚙️ Preparing build..."
autoreconf -i

echo "🔧 Configuring..."
./configure

echo "🚀 Compiling aria2 (this may take a while)..."
make -j$(nproc)

# === Install if sudo available ===
if command -v sudo >/dev/null 2>&1; then
    echo "📂 Installing globally..."
    sudo make install || true
fi

# === Verify build ===
if [ -f "./src/aria2c" ]; then
    echo "✅ Build successful!"
    echo "You can run aria2 with:"
    echo "   ./src/aria2c --version"
else
    echo "❌ Build failed!"
    exit 1
fi
