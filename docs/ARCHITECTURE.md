# KenOS v10 Architecture

## Core

- kenos.py
- command_manager.py
- plugin_loader.py

## AI

- core/router.py
- core/jarvis.py
- core/nlp.py
- core/memory.py
- core/history.py

## Device

- core/device.py
- core/voice.py

## Plugins

Each plugin should expose:

- NAME
- DESCRIPTION
- SKILLS (optional)
- run(args)

The AI should never execute hardware directly.
All actions must go through plugins.
