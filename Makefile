.PHONY: help install uninstall

.DEFAULT_GOAL := help

SOURCE = clara.py
TARGET = clara
LOCAL_BIN = ~/.local/bin
SYSTEM_DIR = ~/.clara
LOGS_DIR = $(SYSTEM_DIR)/logs
ENV_FILE = $(SYSTEM_DIR)/.env

help:
	@echo "Usage: make [TARGET]"
	@echo "Targets:"
	@echo "  [install]  Install for the current user ($(LOCAL_BIN)/$(TARGET))"
	@echo "  [uninstall]  Uninstall for the current user ($(LOCAL_BIN)/$(TARGET))"

install:
	mkdir -p $(LOCAL_BIN)
	mkdir -p $(LOGS_DIR)
	cp $(SOURCE) $(LOCAL_BIN)/$(TARGET)
	chmod +x $(LOCAL_BIN)/$(TARGET)
	@if [ ! -f $(ENV_FILE) ]; then \
		read -p "GEMINI_API_KEY: " key; \
		echo "GEMINI_API_KEY=$$key" > $(ENV_FILE); \
	fi
	@echo "Clara AI assistant installed!"

uninstall:
	rm -f $(LOCAL_BIN)/$(TARGET)
	@echo "Clara AI assistant uninstalled!"
