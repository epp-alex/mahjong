import pygame
import os
import random
import json
import sys
import math

# ============================================================================
# PFAD-LOGIK
# ============================================================================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ============================================================================
# SPRACHUNTERSTÜTZUNG / LANGUAGE SUPPORT
# ============================================================================
LANGUAGES = {
    "Deutsch": {
        "menu_title":       "MAHJONG AUSWAHL",
        "menu_images_info": "{n} Bilder vorhanden  —  jedes Level wählt zufällig aus ALLEN Bildern",
        "menu_esc":         "ESC = Beenden",
        "menu_pairs_info":  "{pairs} Paare, {rows}×{cols}",
        "menu_1player":     "Einzelspieler",
        "menu_2player":     "2 Spieler",
        "hud_level":        "Level",
        "hud_pairs":        "Paare",
        "hud_clicks":       "Klicks",
        "hud_volume":       "Lautstärke",
        "hud_volume_hint":  "+/- zum Ändern",
        "hud_turn":         "{name} ist dran",
        "hud_score":        "{p1}: {s1}  |  {p2}: {s2}",
        "win_title":        "GEWONNEN!",
        "win_clicks":       "Klicks: {n}",
        "win_hint":         "LEERTASTE: Menü  |  ESC: Beenden",
        "win_2p_winner":    "{name} gewinnt!",
        "win_2p_draw":      "Unentschieden!",
        "win_2p_score":     "{p1}: {s1} Paare  —  {p2}: {s2} Paare",
        "lang_title":       "Sprache wählen",
        "level_easy":       "Einfach",
        "level_medium":     "Mittel",
        "level_hard":       "Schwer",
        "level_expert":     "EXPERT",
        "player1":          "Spieler 1",
        "player2":          "Spieler 2",
    },
    "English": {
        "menu_title":       "MAHJONG — SELECT LEVEL",
        "menu_images_info": "{n} images available  —  each level picks randomly from ALL images",
        "menu_esc":         "ESC = Quit",
        "menu_pairs_info":  "{pairs} pairs, {rows}×{cols}",
        "menu_1player":     "Single Player",
        "menu_2player":     "2 Players",
        "hud_level":        "Level",
        "hud_pairs":        "Pairs",
        "hud_clicks":       "Clicks",
        "hud_volume":       "Volume",
        "hud_volume_hint":  "+/- to change",
        "hud_turn":         "{name}'s turn",
        "hud_score":        "{p1}: {s1}  |  {p2}: {s2}",
        "win_title":        "YOU WIN!",
        "win_clicks":       "Clicks: {n}",
        "win_hint":         "SPACE: Menu  |  ESC: Quit",
        "win_2p_winner":    "{name} wins!",
        "win_2p_draw":      "It's a draw!",
        "win_2p_score":     "{p1}: {s1} pairs  —  {p2}: {s2} pairs",
        "lang_title":       "Choose language",
        "level_easy":       "Easy",
        "level_medium":     "Medium",
        "level_hard":       "Hard",
        "level_expert":     "EXPERT",
        "player1":          "Player 1",
        "player2":          "Player 2",
    },
    "Français": {
        "menu_title":       "SÉLECTION MAHJONG",
        "menu_images_info": "{n} images disponibles — chaque niveau choisit au hasard parmi TOUTES les images",
        "menu_esc":         "ESC = Quitter",
        "menu_pairs_info":  "{pairs} paires, {rows}×{cols}",
        "menu_1player":     "Solo",
        "menu_2player":     "2 Joueurs",
        "hud_level":        "Niveau",
        "hud_pairs":        "Paires",
        "hud_clicks":       "Clics",
        "hud_volume":       "Volume",
        "hud_volume_hint":  "+/- pour modifier",
        "hud_turn":         "Tour de {name}",
        "hud_score":        "{p1}: {s1}  |  {p2}: {s2}",
        "win_title":        "GAGNÉ !",
        "win_clicks":       "Clics : {n}",
        "win_hint":         "ESPACE : Menu  |  ESC : Quitter",
        "win_2p_winner":    "{name} gagne !",
        "win_2p_draw":      "Égalité !",
        "win_2p_score":     "{p1}: {s1} paires  —  {p2}: {s2} paires",
        "lang_title":       "Choisir la langue",
        "level_easy":       "Facile",
        "level_medium":     "Moyen",
        "level_hard":       "Difficile",
        "level_expert":     "EXPERT",
        "player1":          "Joueur 1",
        "player2":          "Joueur 2",
    },
    "Español": {
        "menu_title":       "SELECCIÓN MAHJONG",
        "menu_images_info": "{n} imágenes disponibles — cada nivel elige al azar de TODAS las imágenes",
        "menu_esc":         "ESC = Salir",
        "menu_pairs_info":  "{pairs} parejas, {rows}×{cols}",
        "menu_1player":     "Un jugador",
        "menu_2player":     "2 Jugadores",
        "hud_level":        "Nivel",
        "hud_pairs":        "Parejas",
        "hud_clicks":       "Clics",
        "hud_volume":       "Volumen",
        "hud_volume_hint":  "+/- para cambiar",
        "hud_turn":         "Turno de {name}",
        "hud_score":        "{p1}: {s1}  |  {p2}: {s2}",
        "win_title":        "¡HAS GANADO!",
        "win_clicks":       "Clics: {n}",
        "win_hint":         "ESPACIO: Menú  |  ESC: Salir",
        "win_2p_winner":    "¡{name} gana!",
        "win_2p_draw":      "¡Empate!",
        "win_2p_score":     "{p1}: {s1} parejas  —  {p2}: {s2} parejas",
        "lang_title":       "Seleccionar idioma",
        "level_easy":       "Fácil",
        "level_medium":     "Medio",
        "level_hard":       "Difícil",
        "level_expert":     "EXPERTO",
        "player1":          "Jugador 1",
        "player2":          "Jugador 2",
    },
    "Italiano": {
        "menu_title":       "SELEZIONE MAHJONG",
        "menu_images_info": "{n} immagini disponibili — ogni livello sceglie casualmente da TUTTE le immagini",
        "menu_esc":         "ESC = Esci",
        "menu_pairs_info":  "{pairs} coppie, {rows}×{cols}",
        "menu_1player":     "Giocatore singolo",
        "menu_2player":     "2 Giocatori",
        "hud_level":        "Livello",
        "hud_pairs":        "Coppie",
        "hud_clicks":       "Clic",
        "hud_volume":       "Volume",
        "hud_volume_hint":  "+/- per modificare",
        "hud_turn":         "Turno di {name}",
        "hud_score":        "{p1}: {s1}  |  {p2}: {s2}",
        "win_title":        "HAI VINTO!",
        "win_clicks":       "Clic: {n}",
        "win_hint":         "SPAZIO: Menu  |  ESC: Esci",
        "win_2p_winner":    "{name} vince!",
        "win_2p_draw":      "Pareggio!",
        "win_2p_score":     "{p1}: {s1} coppie  —  {p2}: {s2} coppie",
        "lang_title":       "Scegli la lingua",
        "level_easy":       "Facile",
        "level_medium":     "Medio",
        "level_hard":       "Difficile",
        "level_expert":     "ESPERTO",
        "player1":          "Giocatore 1",
        "player2":          "Giocatore 2",
    },
    "Português": {
        "menu_title":       "SELEÇÃO MAHJONG",
        "menu_images_info": "{n} imagens disponíveis — cada nível escolhe aleatoriamente de TODAS as imagens",
        "menu_esc":         "ESC = Sair",
        "menu_pairs_info":  "{pairs} pares, {rows}×{cols}",
        "menu_1player":     "Um jogador",
        "menu_2player":     "2 Jogadores",
        "hud_level":        "Nível",
        "hud_pairs":        "Pares",
        "hud_clicks":       "Cliques",
        "hud_volume":       "Volume",
        "hud_volume_hint":  "+/- para alterar",
        "hud_turn":         "Vez de {name}",
        "hud_score":        "{p1}: {s1}  |  {p2}: {s2}",
        "win_title":        "GANHOU!",
        "win_clicks":       "Cliques: {n}",
        "win_hint":         "ESPAÇO: Menu  |  ESC: Sair",
        "win_2p_winner":    "{name} vence!",
        "win_2p_draw":      "Empate!",
        "win_2p_score":     "{p1}: {s1} pares  —  {p2}: {s2} pares",
        "lang_title":       "Escolher idioma",
        "level_easy":       "Fácil",
        "level_medium":     "Médio",
        "level_hard":       "Difícil",
        "level_expert":     "ESPECIALISTA",
        "player1":          "Jogador 1",
        "player2":          "Jogador 2",
    },
    "Nederlands": {
        "menu_title":       "MAHJONG SELECTIE",
        "menu_images_info": "{n} afbeeldingen beschikbaar — elk niveau kiest willekeurig uit ALLE afbeeldingen",
        "menu_esc":         "ESC = Verlaten",
        "menu_pairs_info":  "{pairs} paren, {rows}×{cols}",
        "menu_1player":     "Één speler",
        "menu_2player":     "2 Spelers",
        "hud_level":        "Niveau",
        "hud_pairs":        "Paren",
        "hud_clicks":       "Klikken",
        "hud_volume":       "Volume",
        "hud_volume_hint":  "+/- om te wijzigen",
        "hud_turn":         "{name} is aan de beurt",
        "hud_score":        "{p1}: {s1}  |  {p2}: {s2}",
        "win_title":        "GEWONNEN!",
        "win_clicks":       "Klikken: {n}",
        "win_hint":         "SPATIEBALK: Menu  |  ESC: Verlaten",
        "win_2p_winner":    "{name} wint!",
        "win_2p_draw":      "Gelijkspel!",
        "win_2p_score":     "{p1}: {s1} paren  —  {p2}: {s2} paren",
        "lang_title":       "Taal kiezen",
        "level_easy":       "Eenvoudig",
        "level_medium":     "Gemiddeld",
        "level_hard":       "Moeilijk",
        "level_expert":     "EXPERT",
        "player1":          "Speler 1",
        "player2":          "Speler 2",
    },
    "Polski": {
        "menu_title":       "WYBÓR MAHJONGA",
        "menu_images_info": "Dostępne obrazy: {n} — każdy poziom wybiera losowo ze WSZYSTKICH obrazów",
        "menu_esc":         "ESC = Wyjście",
        "menu_pairs_info":  "{pairs} par, {rows}×{cols}",
        "menu_1player":     "Jeden gracz",
        "menu_2player":     "2 Graczy",
        "hud_level":        "Poziom",
        "hud_pairs":        "Pary",
        "hud_clicks":       "Kliknięcia",
        "hud_volume":       "Głośność",
        "hud_volume_hint":  "+/- aby zmienić",
        "hud_turn":         "Kolej gracza {name}",
        "hud_score":        "{p1}: {s1}  |  {p2}: {s2}",
        "win_title":        "WYGRANA!",
        "win_clicks":       "Kliknięcia: {n}",
        "win_hint":         "SPACJA: Menu  |  ESC: Wyjście",
        "win_2p_winner":    "{name} wygrywa!",
        "win_2p_draw":      "Remis!",
        "win_2p_score":     "{p1}: {s1} par  —  {p2}: {s2} par",
        "lang_title":       "Wybierz język",
        "level_easy":       "Łatwy",
        "level_medium":     "Średni",
        "level_hard":       "Trudny",
        "level_expert":     "EKSPERT",
        "player1":          "Gracz 1",
        "player2":          "Gracz 2",
    },
    "Русский": {
        "menu_title":       "ВЫБОР МАДЖОНГА",
        "menu_images_info": "Доступно изображений: {n} — каждый уровень выбирает случайно из ВСЕХ",
        "menu_esc":         "ESC = Выход",
        "menu_pairs_info":  "{pairs} пар, {rows}×{cols}",
        "menu_1player":     "Один игрок",
        "menu_2player":     "2 Игрока",
        "hud_level":        "Уровень",
        "hud_pairs":        "Пары",
        "hud_clicks":       "Клики",
        "hud_volume":       "Громкость",
        "hud_volume_hint":  "+/- для изменения",
        "hud_turn":         "Ход игрока {name}",
        "hud_score":        "{p1}: {s1}  |  {p2}: {s2}",
        "win_title":        "ПОБЕДА!",
        "win_clicks":       "Кликов: {n}",
        "win_hint":         "ПРОБЕЛ: Меню  |  ESC: Выход",
        "win_2p_winner":    "{name} побеждает!",
        "win_2p_draw":      "Ничья!",
        "win_2p_score":     "{p1}: {s1} пар  —  {p2}: {s2} пар",
        "lang_title":       "Выберите язык",
        "level_easy":       "Лёгкий",
        "level_medium":     "Средний",
        "level_hard":       "Сложный",
        "level_expert":     "ЭКСПЕРТ",
        "player1":          "Игрок 1",
        "player2":          "Игрок 2",
    },
    "Українська": {
        "menu_title":       "ВИБІР МАДЖОНГУ",
        "menu_images_info": "Доступно зображень: {n} — кожен рівень вибирає випадково з УСІХ",
        "menu_esc":         "ESC = Вихід",
        "menu_pairs_info":  "{pairs} пар, {rows}×{cols}",
        "menu_1player":     "Один гравець",
        "menu_2player":     "2 Гравці",
        "hud_level":        "Рівень",
        "hud_pairs":        "Пари",
        "hud_clicks":       "Кліки",
        "hud_volume":       "Гучність",
        "hud_volume_hint":  "+/- для зміни",
        "hud_turn":         "Хід гравця {name}",
        "hud_score":        "{p1}: {s1}  |  {p2}: {s2}",
        "win_title":        "ПЕРЕМОГА!",
        "win_clicks":       "Кліків: {n}",
        "win_hint":         "ПРОБІЛ: Меню  |  ESC: Вихід",
        "win_2p_winner":    "{name} перемагає!",
        "win_2p_draw":      "Нічия!",
        "win_2p_score":     "{p1}: {s1} пар  —  {p2}: {s2} пар",
        "lang_title":       "Оберіть мову",
        "level_easy":       "Легкий",
        "level_medium":     "Середній",
        "level_hard":       "Важкий",
        "level_expert":     "ЕКСПЕРТ",
        "player1":          "Гравець 1",
        "player2":          "Гравець 2",
    },
    "Türkçe": {
        "menu_title":       "MAHJONG SEÇİMİ",
        "menu_images_info": "{n} görsel mevcut — her seviye TÜM görsellerden rastgele seçer",
        "menu_esc":         "ESC = Çıkış",
        "menu_pairs_info":  "{pairs} çift, {rows}×{cols}",
        "menu_1player":     "Tek oyuncu",
        "menu_2player":     "2 Oyuncu",
        "hud_level":        "Seviye",
        "hud_pairs":        "Çiftler",
        "hud_clicks":       "Tıklama",
        "hud_volume":       "Ses",
        "hud_volume_hint":  "+/- ile değiştir",
        "hud_turn":         "{name} oynuyor",
        "hud_score":        "{p1}: {s1}  |  {p2}: {s2}",
        "win_title":        "KAZANDIN!",
        "win_clicks":       "Tıklama: {n}",
        "win_hint":         "BOŞLUK: Menü  |  ESC: Çıkış",
        "win_2p_winner":    "{name} kazandı!",
        "win_2p_draw":      "Beraberlik!",
        "win_2p_score":     "{p1}: {s1} çift  —  {p2}: {s2} çift",
        "lang_title":       "Dil seçin",
        "level_easy":       "Kolay",
        "level_medium":     "Orta",
        "level_hard":       "Zor",
        "level_expert":     "UZMAN",
        "player1":          "Oyuncu 1",
        "player2":          "Oyuncu 2",
    },
    "Magyar": {
        "menu_title":       "MAHJONG KIVÁLASZTÁS",
        "menu_images_info": "{n} kép elérhető — minden szint véletlenszerűen választ AZ ÖSSZES kép közül",
        "menu_esc":         "ESC = Kilépés",
        "menu_pairs_info":  "{pairs} pár, {rows}×{cols}",
        "menu_1player":     "Egy játékos",
        "menu_2player":     "2 Játékos",
        "hud_level":        "Szint",
        "hud_pairs":        "Párok",
        "hud_clicks":       "Kattintás",
        "hud_volume":       "Hangerő",
        "hud_volume_hint":  "+/- a változtatáshoz",
        "hud_turn":         "{name} következik",
        "hud_score":        "{p1}: {s1}  |  {p2}: {s2}",
        "win_title":        "NYERTÉL!",
        "win_clicks":       "Kattintás: {n}",
        "win_hint":         "SZÓKÖZ: Menü  |  ESC: Kilépés",
        "win_2p_winner":    "{name} nyert!",
        "win_2p_draw":      "Döntetlen!",
        "win_2p_score":     "{p1}: {s1} pár  —  {p2}: {s2} pár",
        "lang_title":       "Válasszon nyelvet",
        "level_easy":       "Könnyű",
        "level_medium":     "Közepes",
        "level_hard":       "Nehéz",
        "level_expert":     "SZAKÉRTŐ",
        "player1":          "1. játékos",
        "player2":          "2. játékos",
    },
   "Čeština": {
        "menu_title":       "VÝBĚR MAHJONGU",
        "menu_images_info": "K dispozici je {n} obrázků — každá úroveň vybírá náhodně ze VŠECH obrázků",
        "menu_esc":         "ESC = Ukončit",
        "menu_pairs_info":  "{pairs} párů, {rows}×{cols}",
        "hud_level":        "Úroveň",
        "hud_pairs":         "Páry",
        "hud_clicks":        "Kliknutí",
        "hud_volume":        "Hlasitost",
        "hud_volume_hint":   "+/- pro změnu",
        "win_title":        "VYHRÁL JSI!",
        "win_clicks":       "Kliknutí: {n}",
        "win_hint":         "MEZERNÍK: Menu  |  ESC: Ukončit",
        "lang_title":       "Vyberte jazyk",
        "level_easy":       "Snadná",
        "level_medium":     "Střední",
        "level_hard":       "Těžká",
        "level_expert":     "EXPERT",
    },
    "Svenska": {
        "menu_title":       "MAHJONG — VÄLJ NIVÅ",
        "menu_images_info": "{n} bilder tillgängliga — varje nivå väljer slumpmässigt bland ALLA bilder",
        "menu_esc":         "ESC = Avsluta",
        "menu_pairs_info":  "{pairs} par, {rows}×{cols}",
        "hud_level":        "Nivå",
        "hud_pairs":         "Par",
        "hud_clicks":       "Klick",
        "hud_volume":       "Volym",
        "hud_volume_hint":  "+/- för att ändra",
        "win_title":        "DU VANN!",
        "win_clicks":       "Klick: {n}",
        "win_hint":         "BLANKSTEG: Meny  |  ESC: Avsluta",
        "lang_title":       "Välj språk",
        "level_easy":       "Lätt",
        "level_medium":     "Medel",
        "level_hard":       "Svår",
        "level_expert":     "EXPERT",
    },
    "Română": {
        "menu_title":       "SELECȚIE MAHJONG",
        "menu_images_info": "{n} imagini disponibile — fiecare nivel alege aleatoriu din TOATE imaginile",
        "menu_esc":         "ESC = Ieșire",
        "menu_pairs_info":  "{pairs} perechi, {rows}×{cols}",
        "hud_level":        "Nivel",
        "hud_pairs":         "Perechi",
        "hud_clicks":       "Click-uri",
        "hud_volume":       "Volum",
        "hud_volume_hint":  "+/- pentru modificare",
        "win_title":        "AI CÂȘTIGAT!",
        "win_clicks":       "Click-uri: {n}",
        "win_hint":         "SPAȚIU: Meniu  |  ESC: Ieșire",
        "lang_title":       "Alege limba",
        "level_easy":       "Ușor",
        "level_medium":     "Mediu",
        "level_hard":       "Greu",
        "level_expert":     "EXPERT",
    },
    "Ελληνικά": {
        "menu_title":       "ΕΠΙΛΟΓΗ MAHJONG",
        "menu_images_info": "{n} διαθέσιμες εικόνες — κάθε επίπεδο επιλέγει τυχαία από ΟΛΕΣ τις εικόνες",
        "menu_esc":         "ESC = Έξοδος",
        "menu_pairs_info":  "{pairs} ζευγάρια, {rows}×{cols}",
        "hud_level":        "Επίπεδο",
        "hud_pairs":         "Ζευγάρια",
        "hud_clicks":       "Κλικ",
        "hud_volume":       "Ένταση",
        "hud_volume_hint":  "+/- για αλλαγή",
        "win_title":        "ΚΕΡΔΙΣΕΣ!",
        "win_clicks":       "Κλικ: {n}",
        "win_hint":         "SPACE: Μενού  |  ESC: Έξοδος",
        "lang_title":       "Επιλογή γλώσσας",
        "level_easy":       "Εύκολο",
        "level_medium":     "Μέτριο",
        "level_hard":       "Δύσκολο",
        "level_expert":     "ΕΜΠΕΙΡΟ",
    },


}

# Aktuell gewählte Sprache (wird durch language_select() / load_settings() gesetzt)
_current_lang = "English"


# ============================================================================
# EINSTELLUNGEN SPEICHERN / SETTINGS PERSISTENCE
# ============================================================================
def get_settings_path():
    """Gibt den plattformgerechten AppData-Pfad zurück."""
    app_name = "Mahjong"
    if sys.platform == "win32":
        base = os.environ.get("APPDATA", os.path.expanduser("~"))
    elif sys.platform == "darwin":
        base = os.path.join(os.path.expanduser("~"), "Library", "Application Support")
    else:
        # Linux / andere Unix-Systeme
        base = os.environ.get("XDG_CONFIG_HOME", os.path.join(os.path.expanduser("~"), ".config"))
    folder = os.path.join(base, app_name)
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "settings.json")


def load_settings():
    """Lädt gespeicherte Einstellungen; gibt Defaults zurück wenn nicht vorhanden."""
    global _current_lang
    try:
        with open(get_settings_path(), "r", encoding="utf-8") as f:
            data = json.load(f)
        lang = data.get("language", "Deutsch")
        if lang in LANGUAGES:
            _current_lang = lang
    except Exception:
        pass  # Erste Ausführung oder Datei fehlt → Defaults behalten


def save_settings():
    """Speichert aktuelle Einstellungen in AppData."""
    try:
        data = {"language": _current_lang}
        with open(get_settings_path(), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[Warnung] Einstellungen konnten nicht gespeichert werden: {e}")


# ============================================================================
# ÜBERSETZUNG / TRANSLATION
# ============================================================================
def T(key, **kwargs):
    """Gibt den übersetzten Text für den Schlüssel zurück.
    Platzhalter werden per kwargs ersetzt: T('win_clicks', n=42) → 'Klicks: 42'"""
    text = LANGUAGES.get(_current_lang, LANGUAGES["Deutsch"]).get(key, key)
    return text.format(**kwargs) if kwargs else text


def language_select():
    """Zeigt einen Sprachauswahl-Screen (2-Spalten-Layout) und speichert die Wahl."""
    global _current_lang
    lang_names = list(LANGUAGES.keys())

    # Farben pro Sprache — einfach neue Sprachen hier ergänzen
    lang_colors = {
        "Deutsch":    (0,   100, 200),
        "English":    (180,  40,  40),
        "Français":   (0,   140,  70),
        "Español":    (200, 140,   0),
        "Italiano":   (20,  140,  80),
        "Português":  (0,   160, 100),
        "Nederlands": (220, 100,   0),
        "Polski":     (160,  30,  30),
        "Русский":    (140,   0, 180),
        "Українська": (0,   120, 220),
        "Türkçe":     (180,  50,  50),
        "Magyar":     (80,   60, 180),
        "Čeština":    (120,  80,  40),
        "Svenska":    (0,    90, 160),
        "Română":     (140, 110,  20),
        "Ελληνικά":   (30,   70, 150),
    }
    default_color = (80, 80, 160)

    # Layout relativ zur Bildschirmgröße
    BTN_W = min(360, int(SCREEN_W * 0.28))
    BTN_H = max(36,  int(SCREEN_H * 0.055))
    COLS  = 2
    H_GAP = max(12, int(SCREEN_W * 0.015))
    V_GAP = max(8,  int(SCREEN_H * 0.012))

    while True:
        screen.fill((20, 20, 35))

        # Titel
        title = FONT_M.render("Sprache  /  Language", True, (255, 255, 255))
        screen.blit(title, title.get_rect(center=(SCREEN_W // 2, max(40, int(SCREEN_H * 0.07)))))

        hint = FONT_XS.render("ESC = Zurück / Back", True, (80, 80, 80))
        screen.blit(hint, hint.get_rect(center=(SCREEN_W // 2, SCREEN_H - int(SCREEN_H * 0.03))))

        # Grid-Ursprung berechnen
        rows = math.ceil(len(lang_names) / COLS)
        grid_w = COLS * BTN_W + (COLS - 1) * H_GAP
        grid_h = rows * BTN_H + (rows - 1) * V_GAP
        origin_x = (SCREEN_W - grid_w) // 2
        origin_y = (SCREEN_H - grid_h) // 2 + 30   # leicht nach unten, Titel hat Platz

        buttons = {}
        mouse_pos = pygame.mouse.get_pos()

        for i, lang in enumerate(lang_names):
            col = i % COLS
            row = i // COLS
            x = origin_x + col * (BTN_W + H_GAP)
            y = origin_y + row * (BTN_H + V_GAP)
            rect = pygame.Rect(x, y, BTN_W, BTN_H)
            buttons[lang] = rect

            base_col = lang_colors.get(lang, default_color)
            hover    = rect.collidepoint(mouse_pos)
            active   = (lang == _current_lang)

            if hover:
                draw_col = tuple(min(255, c + 70) for c in base_col)
                text_col = (10, 10, 10)
                pygame.draw.rect(screen, (255, 215, 0), rect.inflate(8, 8), border_radius=16)
            elif active:
                draw_col = tuple(min(255, c + 40) for c in base_col)
                text_col = (255, 255, 255)
                pygame.draw.rect(screen, (255, 255, 255), rect.inflate(6, 6), 3, border_radius=16)
            else:
                draw_col = base_col
                text_col = (255, 255, 255)

            pygame.draw.rect(screen, draw_col, rect, border_radius=14)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1, border_radius=14)

            txt = FONT_S.render(lang, True, text_col)
            screen.blit(txt, txt.get_rect(center=rect.center))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return  # zurück ins Hauptmenü
            if event.type == pygame.MOUSEBUTTONDOWN:
                for lang, r in buttons.items():
                    if r.collidepoint(event.pos):
                        _current_lang = lang
                        save_settings()
                        return


# ============================================================================
# KONFIGURATION
# ============================================================================
def load_config():
    config_p = resource_path("mahjong_config.json")
    try:
        with open(config_p, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {
            "game": {"audio": {"initial_volume": 0.3}},
            "tiles": {"image_folder": "bild"}
        }

CFG = load_config()

# Zähle verfügbare Bilder
def count_images():
    img_folder = resource_path(CFG["tiles"]["image_folder"])
    try:
        return len([f for f in os.listdir(img_folder) if f.endswith(".png")])
    except:
        return 40

TOTAL_IMAGES = count_images()
print(f"[INFO] {TOTAL_IMAGES} Bilder gefunden in '{CFG['tiles']['image_folder']}'")

# Berechne Levels dynamisch anhand der Bildanzahl
def build_levels():
    # Schlüssel sind interne IDs; Anzeigename wird via T() zur Laufzeit geholt
    levels = {}
    levels["level_easy"]   = {"rows": 4,  "cols": 4,  "total_pairs": 8,  "spacing": 20}
    levels["level_medium"] = {"rows": 4,  "cols": 8,  "total_pairs": 16, "spacing": 15}
    levels["level_hard"]   = {"rows": 5,  "cols": 10, "total_pairs": 25, "spacing": 10}
    levels["level_expert"] = {"rows": 8,  "cols": 10, "total_pairs": 40, "spacing": 8}
    return levels

LEVELS = build_levels()

# ============================================================================
# INITIALISIERUNG
# ============================================================================
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()

# Plattformübergreifendes Fenster
_info = pygame.display.Info()
_native_w, _native_h = _info.current_w, _info.current_h

if sys.platform == "darwin":
    # Mac: echter Vollbildmodus
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    SCREEN_W, SCREEN_H = screen.get_width(), screen.get_height()
elif sys.platform == "win32":
    # Windows: rahmenlos in nativer Auflösung
    screen = pygame.display.set_mode((_native_w, _native_h), pygame.NOFRAME)
    SCREEN_W, SCREEN_H = _native_w, _native_h
else:
    # Linux: maximiertes Fenster — funktioniert auf X11 und Wayland
    # SDL-Hint vor dem Erstellen setzen → Fenster startet maximiert
    os.environ["SDL_VIDEO_MAXIMIZE_WINDOW"] = "1"
    screen = pygame.display.set_mode(
        (_native_w, _native_h),
        pygame.RESIZABLE
    )
    SCREEN_W, SCREEN_H = screen.get_width(), screen.get_height()

pygame.display.set_caption("Mahjong")
clock = pygame.time.Clock()

# ============================================================================
# UNICODE-FONT-SYSTEM (Kyrillisch, Latein, Türkisch, Ungarisch etc.)
# ============================================================================
# Kandidaten-Fonts mit guter Unicode-Abdeckung — werden der Reihe nach ausprobiert
_FONT_CANDIDATES = [
    # Linux
    "dejavusans", "freesans", "liberationsans", "notosans",
    # Windows
    "segoeui", "arial", "calibri",
    # Mac
    "helveticaneue", "helvetica",
    # Universell
    "unifont",
]

_font_cache: dict = {}


def _find_system_font(candidates: list) -> str | None:
    """Gibt den ersten gefundenen Systemfont-Namen zurück, oder None."""
    available = set(f.lower() for f in pygame.font.get_fonts())
    for name in candidates:
        if name.lower().replace(" ", "") in available or name.lower() in available:
            return name
    return None


_best_font = _find_system_font(_FONT_CANDIDATES)
print(f"[FONT] Gewählt: {_best_font or '(keiner gefunden — pygame default)'}")


def get_font(size: int) -> pygame.font.Font:
    """Gibt den Unicode-fähigen Font in der gewünschten Größe zurück (gecacht)."""
    if size not in _font_cache:
        if _best_font:
            try:
                _font_cache[size] = pygame.font.SysFont(_best_font, size)
            except Exception:
                _font_cache[size] = pygame.font.Font(None, size)
        else:
            _font_cache[size] = pygame.font.Font(None, size)
    return _font_cache[size]


class _DynFont:
    """Wrapper damit FONT_L/M/S/XS weiterhin wie gewohnt nutzbar sind."""
    def __init__(self, size: int):
        self._size = size
    def render(self, text, antialias, color, bg=None):
        f = get_font(self._size)
        return f.render(text, antialias, color, bg) if bg is not None else f.render(text, antialias, color)
    def size(self, text):
        return get_font(self._size).size(text)
    def get_height(self):
        return get_font(self._size).get_height()


FONT_L  = _DynFont(max(36, SCREEN_H // 18))   # Titel Hauptmenü  (~60px bei 1080p)
FONT_M  = _DynFont(max(24, SCREEN_H // 28))   # Zwischen-Titel   (~38px bei 1080p)
FONT_S  = _DynFont(max(18, SCREEN_H // 40))   # Button-Text      (~27px bei 1080p)
FONT_XS = _DynFont(max(14, SCREEN_H // 60))   # Info / Hinweise  (~18px bei 1080p)

# ============================================================================
# KLASSEN
# ============================================================================
class Particle:
    def __init__(self, x, y, color):
        self.x, self.y = x, y
        self.color = color
        self.vx, self.vy = random.uniform(-5, 5), random.uniform(-5, 5)
        self.lifetime = 30
        self.size = random.randint(3, 6)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1
        self.size = max(0, self.size - 0.1)

    def draw(self, surf):
        if self.lifetime > 0:
            pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), int(self.size))


class Lightning:
    def __init__(self):
        self.points = [(random.randint(0, SCREEN_W), 0)]
        for i in range(1, 10):
            self.points.append((
                self.points[-1][0] + random.randint(-120, 120),
                i * (SCREEN_H // 9)
            ))
        self.age, self.max_age = 0, 15

    def draw(self, surf):
        if self.age < self.max_age:
            pygame.draw.lines(surf, (255, 255, 180), False, self.points, 4)
            self.age += 1


class Tile:
    def __init__(self, x, y, tid, img, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.tid = tid
        self.img = img
        self.flipped = False
        self.matched = False
        self.hover = False

    def draw(self, surf):
        if not self.matched:
            bg = (255, 255, 255) if self.flipped else (45, 45, 60)
            if self.hover and not self.flipped:
                bg = (70, 70, 100)
            pygame.draw.rect(surf, bg, self.rect, border_radius=8)
            pygame.draw.rect(surf, (200, 200, 200), self.rect, 1, border_radius=8)
            if self.flipped and self.img:
                i_rect = self.img.get_rect(center=self.rect.center)
                surf.blit(self.img, i_rect)


# ============================================================================
# SPIEL
# ============================================================================
class MahjongGame:
    def __init__(self, level_name, two_player=False):
        pygame.mixer.music.stop()
        l_cfg = LEVELS[level_name]
        self.level_name  = level_name
        self.rows        = l_cfg["rows"]
        self.cols        = l_cfg["cols"]
        self.total_pairs = l_cfg["total_pairs"]
        self.spacing     = l_cfg["spacing"]
        self.two_player  = two_player

        self.tiles      = []
        self.flipped    = []
        self.particles  = []
        self.lightnings = []
        self.clicks     = 0
        self.matches    = 0
        self.won        = False
        self.win_timer  = 0
        self.music_stopped = False
        self.volume     = CFG["game"]["audio"].get("initial_volume", 0.3)

        # 2-Spieler-Zustand
        self.current_player = 0                          # 0 = Spieler 1, 1 = Spieler 2
        self.scores         = [0, 0]                     # gesammelte Paare pro Spieler
        self.player_names   = [T("player1"), T("player2")]
        # Jeder Spieler bekommt eine eigene Hintergrundfarbe für die Statusleiste
        self.player_colors  = [(80, 160, 255), (255, 120, 80)]

        # Dynamische Steingröße
        avail_w = SCREEN_W - (self.cols + 1) * self.spacing
        avail_h = (SCREEN_H - 160) - (self.rows + 1) * self.spacing
        max_tw  = avail_w // self.cols
        max_th  = avail_h // self.rows

        if max_tw < max_th * 0.62:
            self.tw = max_tw
            self.th = int(self.tw / 0.62)
        else:
            self.th = max_th
            self.tw = int(self.th * 0.62)

        # Mindestgröße
        self.tw = max(self.tw, 20)
        self.th = max(self.th, 28)

        self.load_assets()
        self.setup_grid()

    def load_assets(self):
        self.images = {}
        img_folder = resource_path(CFG["tiles"]["image_folder"])
        try:
            available = sorted([f for f in os.listdir(img_folder) if f.endswith(".png")])
            random.shuffle(available)
            # Verwende so viele Bilder wie benötigt (rotiere wenn zu wenig)
            selected = []
            while len(selected) < self.total_pairs:
                selected.extend(available)
            selected = selected[:self.total_pairs]
            random.shuffle(selected)

            for i, f_name in enumerate(selected):
                img = pygame.image.load(os.path.join(img_folder, f_name)).convert_alpha()
                self.images[i + 1] = pygame.transform.smoothscale(
                    img, (max(1, self.tw - 6), max(1, self.th - 6))
                )
        except Exception as e:
            print(f"[Fehler] Bilder laden: {e}")

        try:
            self.snd_match = pygame.mixer.Sound(resource_path("001.wav"))
            pygame.mixer.music.load(resource_path("002.wav"))
            self.update_vol(0)
        except:
            self.snd_match = None

    def update_vol(self, step):
        self.volume = max(0.0, min(1.0, self.volume + step))
        if self.snd_match:
            self.snd_match.set_volume(self.volume)
        pygame.mixer.music.set_volume(self.volume)

    def setup_grid(self):
        ids = list(range(1, self.total_pairs + 1)) * 2
        random.shuffle(ids)
        gw = self.cols * self.tw + (self.cols - 1) * self.spacing
        gh = self.rows * self.th + (self.rows - 1) * self.spacing
        sx = (SCREEN_W - gw) // 2
        sy = (SCREEN_H - gh) // 2 + 40
        for i, tid in enumerate(ids):
            c = i % self.cols
            r = i // self.cols
            tx = sx + c * (self.tw + self.spacing)
            ty = sy + r * (self.th + self.spacing)
            self.tiles.append(Tile(tx, ty, tid, self.images.get(tid), self.tw, self.th))

    def create_explosion(self, x, y):
        for _ in range(12):
            self.particles.append(
                Particle(x, y, random.choice([(255,255,255),(255,215,0),(41,128,185)]))
            )

    def update(self, dt):
        if self.won:
            self.win_timer += dt
            if self.win_timer >= 7000 and not self.music_stopped:
                pygame.mixer.music.stop()
                self.music_stopped = True
            if self.win_timer < 7000 and random.random() < 0.15:
                self.lightnings.append(Lightning())

        for p in self.particles[:]:
            p.update()
            if p.lifetime <= 0:
                self.particles.remove(p)
        self.lightnings = [l for l in self.lightnings if l.age < l.max_age]

        m_pos = pygame.mouse.get_pos()
        for t in self.tiles:
            t.hover = t.rect.collidepoint(m_pos)

    def draw(self, surf):
        surf.fill((15, 15, 25))

        # ── Statusleiste ───────────────────────────────────────────────────
        if self.two_player:
            # Hintergrund-Streifen in Spielerfarbe
            hud_col = self.player_colors[self.current_player]
            hud_bg  = tuple(max(0, c - 140) for c in hud_col)
            pygame.draw.rect(surf, hud_bg, (0, 0, SCREEN_W, 38))
            # Wer ist dran
            turn_txt = T("hud_turn", name=self.player_names[self.current_player])
            turn_s   = FONT_XS.render(turn_txt, True, hud_col)
            surf.blit(turn_s, turn_s.get_rect(midleft=(16, 19)))
            # Punktestand
            score_txt = T("hud_score",
                          p1=self.player_names[0], s1=self.scores[0],
                          p2=self.player_names[1], s2=self.scores[1])
            score_s = FONT_XS.render(score_txt, True, (200, 200, 200))
            surf.blit(score_s, score_s.get_rect(midright=(SCREEN_W - 16, 19)))
        else:
            stats_txt = (
                f"{T('hud_level')}: {T(self.level_name)}  |  "
                f"{T('hud_pairs')}: {self.matches}/{self.total_pairs}  |  "
                f"{T('hud_clicks')}: {self.clicks}  |  "
                f"{T('hud_volume')}: {int(self.volume*100)}%  ({T('hud_volume_hint')})"
            )
            stats = FONT_XS.render(stats_txt, True, (180, 180, 180))
            surf.blit(stats, (SCREEN_W//2 - stats.get_width()//2, 12))

        for t in self.tiles:
            t.draw(surf)
        for p in self.particles:
            p.draw(surf)
        for l in self.lightnings:
            l.draw(surf)

        if self.won:
            ov = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
            ov.fill((0, 0, 0, 220))
            surf.blit(ov, (0, 0))

            if self.two_player:
                s0, s1 = self.scores
                if s0 > s1:
                    winner_txt = T("win_2p_winner", name=self.player_names[0])
                    win_col    = self.player_colors[0]
                elif s1 > s0:
                    winner_txt = T("win_2p_winner", name=self.player_names[1])
                    win_col    = self.player_colors[1]
                else:
                    winner_txt = T("win_2p_draw")
                    win_col    = (255, 215, 0)

                t1 = FONT_L.render(winner_txt, True, win_col)
                surf.blit(t1, t1.get_rect(center=(SCREEN_W//2, SCREEN_H//2 - 90)))

                score_txt = T("win_2p_score",
                              p1=self.player_names[0], s1=s0,
                              p2=self.player_names[1], s2=s1)
                t2 = FONT_M.render(score_txt, True, (255, 255, 255))
                surf.blit(t2, t2.get_rect(center=(SCREEN_W//2, SCREEN_H//2 + 10)))
            else:
                t1 = FONT_L.render(T("win_title"), True, (255, 215, 0))
                surf.blit(t1, t1.get_rect(center=(SCREEN_W//2, SCREEN_H//2 - 80)))
                t2 = FONT_M.render(T("win_clicks", n=self.clicks), True, (255, 255, 255))
                surf.blit(t2, t2.get_rect(center=(SCREEN_W//2, SCREEN_H//2 + 10)))

            t3 = FONT_S.render(T("win_hint"), True, (0, 255, 0))
            surf.blit(t3, t3.get_rect(center=(SCREEN_W//2, SCREEN_H//2 + 90)))

        pygame.display.flip()


# ============================================================================
# MENÜ
# ============================================================================
def main_menu():
    pygame.mixer.music.stop()
    level_colors = {
        "level_easy":   (46, 204, 113),
        "level_medium": (241, 196, 15),
        "level_hard":   (231, 76, 60),
        "level_expert": (41, 128, 185),
    }

    # Layout relativ zur Bildschirmgröße
    BTN_W    = min(480, int(SCREEN_W * 0.42))
    BTN_H    = max(50,  int(SCREEN_H * 0.075))
    BTN_GAP  = max(10,  int(SCREEN_H * 0.018))
    TITLE_Y  = max(50,  int(SCREEN_H * 0.07))
    INFO_Y   = max(80,  int(SCREEN_H * 0.14))

    # Modus: "1p" oder "2p"
    mode = "1p"

    while True:
        screen.fill((20, 20, 35))
        mouse_pos = pygame.mouse.get_pos()

        # Titel
        title = FONT_L.render(T("menu_title"), True, (255, 255, 255))
        screen.blit(title, title.get_rect(center=(SCREEN_W // 2, TITLE_Y)))

        # Bild-Info
        info_txt = FONT_XS.render(T("menu_images_info", n=TOTAL_IMAGES), True, (120, 180, 120))
        screen.blit(info_txt, info_txt.get_rect(center=(SCREEN_W // 2, INFO_Y)))

        # ── Modus-Buttons (1P / 2P) ────────────────────────────────────────
        MB_W = (BTN_W - BTN_GAP) // 2
        MB_H = max(36, int(SCREEN_H * 0.052))
        MODE_Y = int(SCREEN_H * 0.22)

        mode_rects = {}
        for mi, (mkey, mlabel) in enumerate([("1p", T("menu_1player")), ("2p", T("menu_2player"))]):
            mx = SCREEN_W // 2 - BTN_W // 2 + mi * (MB_W + BTN_GAP)
            mrect = pygame.Rect(mx, MODE_Y, MB_W, MB_H)
            mode_rects[mkey] = mrect
            active  = (mode == mkey)
            hover   = mrect.collidepoint(mouse_pos)
            if active:
                bg_col  = (255, 215, 0)
                txt_col = (20, 20, 20)
            elif hover:
                bg_col  = (80, 100, 160)
                txt_col = (255, 255, 255)
            else:
                bg_col  = (40, 50, 90)
                txt_col = (160, 160, 200)
            pygame.draw.rect(screen, bg_col, mrect, border_radius=12)
            pygame.draw.rect(screen, (150, 150, 200), mrect, 1, border_radius=12)
            mtxt = FONT_XS.render(mlabel, True, txt_col)
            screen.blit(mtxt, mtxt.get_rect(center=mrect.center))

        # ── Level-Buttons ──────────────────────────────────────────────────
        level_buttons = {}
        n       = len(LEVELS)
        # Startpunkt unterhalb der Modus-Buttons
        start_y = MODE_Y + MB_H + BTN_GAP * 2

        for i, lvl_key in enumerate(LEVELS.keys()):
            rect = pygame.Rect(0, 0, BTN_W, BTN_H)
            rect.topleft = (SCREEN_W // 2 - BTN_W // 2, start_y + i * (BTN_H + BTN_GAP))
            level_buttons[lvl_key] = rect

            base_col = level_colors.get(lvl_key, (100, 100, 100))
            hover    = rect.collidepoint(mouse_pos)

            if hover:
                draw_col = tuple(min(255, c + 60) for c in base_col)
                text_col = (20, 20, 20)
                pygame.draw.rect(screen, (255, 215, 0), rect.inflate(10, 8), border_radius=16)
            else:
                draw_col = base_col
                text_col = (0, 0, 0)

            pygame.draw.rect(screen, draw_col, rect, border_radius=16)
            pygame.draw.rect(screen, (255, 255, 255), rect, 2, border_radius=16)

            lcfg = LEVELS[lvl_key]
            pairs_info = T("menu_pairs_info", pairs=lcfg["total_pairs"],
                           rows=lcfg["rows"], cols=lcfg["cols"])
            label = f"{T(lvl_key)}  ({pairs_info})"
            txt = FONT_S.render(label, True, text_col)
            if txt.get_width() > BTN_W - 16:
                txt = get_font(max(12, FONT_S._size - 6)).render(label, True, text_col)
            screen.blit(txt, txt.get_rect(center=rect.center))

        # ── Language-Button (unten links) ───────────────────────────────────
        LB_H = max(28, int(SCREEN_H * 0.038))
        LB_W = max(140, int(SCREEN_W * 0.16))
        lang_rect = pygame.Rect(0, 0, LB_W, LB_H)
        lang_rect.bottomleft = (20, SCREEN_H - 14)
        lang_hover = lang_rect.collidepoint(mouse_pos)
        lang_bg    = (60, 80, 140) if lang_hover else (35, 50, 100)
        pygame.draw.rect(screen, lang_bg, lang_rect, border_radius=8)
        pygame.draw.rect(screen, (120, 150, 220), lang_rect, 1, border_radius=8)
        lang_lbl = FONT_XS.render(f"[Lang]  {_current_lang}", True, (200, 220, 255))
        screen.blit(lang_lbl, lang_lbl.get_rect(center=lang_rect.center))

        # ── ESC-Hinweis (unten rechts) ──────────────────────────────────────
        esc_hint = FONT_XS.render(T("menu_esc"), True, (100, 100, 100))
        screen.blit(esc_hint, esc_hint.get_rect(bottomright=(SCREEN_W - 20, SCREEN_H - 14)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT", "1p"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "QUIT", "1p"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lang_rect.collidepoint(event.pos):
                    language_select()
                    continue
                for mkey, mr in mode_rects.items():
                    if mr.collidepoint(event.pos):
                        mode = mkey
                for lvl_key, r in level_buttons.items():
                    if r.collidepoint(event.pos):
                        return lvl_key, mode


# ============================================================================
# MAIN
# ============================================================================
def main():
    load_settings()
    while True:
        result = main_menu()
        if result[0] == "QUIT" or result[0] is None:
            break

        lvl, mode = result
        two_player = (mode == "2p")
        game    = MahjongGame(lvl, two_player=two_player)
        running = True
        delay   = 0
        matched_this_turn = False   # hat der aktuelle Spieler gerade ein Paar gefunden?

        while running:
            dt = clock.tick(60)

            if delay > 0:
                delay -= dt
                if delay <= 0:
                    # Kein Paar → Karten zudecken und Spieler wechseln
                    for t in game.flipped:
                        t.flipped = False
                    game.flipped = []
                    if two_player and not matched_this_turn:
                        game.current_player = 1 - game.current_player
                    matched_this_turn = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE and game.won:
                        running = False
                    if event.key in [pygame.K_PLUS, pygame.K_KP_PLUS]:
                        game.update_vol(0.05)
                    if event.key in [pygame.K_MINUS, pygame.K_KP_MINUS]:
                        game.update_vol(-0.05)

                if event.type == pygame.MOUSEBUTTONDOWN and delay <= 0 and not game.won:
                    for t in game.tiles:
                        if t.rect.collidepoint(event.pos) and not t.flipped and not t.matched:
                            t.flipped = True
                            game.flipped.append(t)
                            game.clicks += 1

                            if len(game.flipped) == 2:
                                if game.flipped[0].tid == game.flipped[1].tid:
                                    # Paar gefunden!
                                    if game.snd_match:
                                        game.snd_match.play()
                                    p1 = game.flipped[0].rect.center
                                    p2 = game.flipped[1].rect.center
                                    game.create_explosion(p1[0], p1[1])
                                    game.create_explosion(p2[0], p2[1])
                                    game.flipped[0].matched = True
                                    game.flipped[1].matched = True
                                    game.matches += 1
                                    if two_player:
                                        game.scores[game.current_player] += 1
                                    game.flipped = []
                                    matched_this_turn = True
                                    if game.matches >= game.total_pairs:
                                        game.won = True
                                        pygame.mixer.music.play(-1)
                                else:
                                    matched_this_turn = False
                                    delay = 900
                            break

            game.update(dt)
            game.draw(screen)

    pygame.quit()


if __name__ == "__main__":
    main()
