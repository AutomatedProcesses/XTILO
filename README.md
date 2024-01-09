# Deterministický jednopáskový Turingův stroj

Deterministický jednopáskový Turingův stroj je teoretický výpočetní model používaný v oblasti informatiky. Jedná se o jednoduchý stroj, který manipuluje se symboly na pásce podle tabulky pravidel. Navzdory své jednoduchosti lze deterministický jednopáskový Turingův stroj použít k modelování jakéhokoli výpočtu, který probíhá v počítači. V deterministickém Turingově stroji pro každý stav a symbol pravidla přesně určují jednu akci, která má být provedena, takže v provozu stroje není žádná nejednoznačnost nebo náhodnost. To je v kontrastu s nedeterministickým Turingovým strojem, kde pravidla mohou v dané situaci umožňovat více než jednu možnou akci. Význam Turingova stroje spočívá v jeho schopnosti modelovat logiku jakéhokoli počítačového algoritmu, což z něj činí základní koncept v teorii výpočetní techniky a studiu toho, co lze efektivně vypočítat.

## Subtitle Klíčové komponenty tohoto modelu zahrnují:
- **Páska**:  Rozdělena na sousední buňky, z nichž každá může obsahovat symbol.
- **Čtecí hlava**: Čte a zapisuje symboly na pásce a může posunout pásku doleva nebo doprava o jednu buňku.
- **Stavový registr**: Obsahuje stav Turingova stroje, který se může měnit v reakci na symbol čtený čtecí hlavou.
- **Konečná tabulka pravidel**: Určuje, co stroj dělá na základě aktuálního stavu a čteného symbolu. Určuje symbol k zápisu, směr posunu pásky a další stav stroje.

V souboru TuringMachine.py je definována třída `TM`, která slouží jako reprezentace deterministického Turingova stroje. Třída obsahuje několik metod:
1. **`__init__`**: Inicializuje Turingův stroj s definovanými parametry, jako jsou stavy, symboly, prázdný symbol, počáteční stav, konečné stavy, přechody a počáteční páska.
2. **`step`**: Provede jednotlivý výpočetní krok stroje. Aktualizuje aktuální stav, symbol na pásce a pozici hlavy podle pravidel přechodů. Pokud není definovaný přechod pro aktuální stav a symbol, vyvolá chybu.
3. **`run`**: Spustí Turingův stroj až do dosažení konečného stavu. Opakovaně volá metodu `step` a zastaví se, když je dosaženo konečného stavu.
4. **`print_trace`**: Vypíše log, který zahrnuje sekvenci stavů, symbolů a akcí provedených Turingovým strojem.
5. **`encode_turing_machine`**: Zakóduje podrobnosti o Turingově stroji do řetězce. Tato metoda bere parametry jako stavy, vstupní abecedu, páskovou abecedu, přechody, počáteční stav, akceptační stav a volitelně odmítací stav. Následně generuje řetězec, který reprezentuje tento Turingův stroj pomocí specifického kódovacího schématu.

V souboru main.py je implementován Turingův stroj realizující součin dvou čísel zadaných v binární soustavě, nicméně lze zadat i definici vlastního Turingova stroje. 

Kód umožňuje uživateli buď zadat vlastní parametry pro Turingův stroj, nebo použít výchozí hodnoty. Zde je stručný přehled toho, co jednotlivé části kódu dělají:
1. **Funkce pro vstupy**: Definovali jste funkce `input_set`, `input_transitions` a `parse_transition` pro zpracování uživatelských vstupů pro různé typy parametrů (množiny a pravidla přechodu). Tyto funkce také uživatelům zobrazují výchozí hodnoty, které mohou použít jednoduchým stiskem Enter.
2. **Výchozí hodnoty**: Předdefinovali jste sadu výchozích hodnot pro stavy, symboly, vstupní abecedu, prázdný symbol, abecedu pásky, počáteční stav, konečné stavy, přechody a počáteční obsah pásky. Tyto výchozí hodnoty představují specifickou konfiguraci Turingova stroje.
3. **Přiřazení uživatelského vstupu nebo výchozích hodnot**: Pro každý parametr Turingova stroje kód buď přijímá uživatelský vstup, nebo používá výchozí hodnoty. To je realizováno pomocí dříve definovaných vstupních funkcí.
4. **Inicializace a spuštění Turingova stroje**: Po shromáždění všech potřebných parametrů váš kód inicializuje instanci Turingova stroje s těmito parametry, spustí ho, vytiskne jeho stopu a poté zakóduje jeho konfiguraci.
5. **Tisk zakódovaného Turingova stroje**: Nakonec je vytisknuta zakódovaná reprezentace Turingova stroje, což je užitečné pro analýzu nebo ukládání konfigurace stroje.

Tento popis nastiňuje fungování Turingova stroje, který provádí binární násobení pomocí rekurzivního přístupu. Popis vysvětluje jak algoritmus stroje, tak jeho teoretický základ:
1. **Zpracování nejpravější číslice**: Stroj začíná pohybem k nejpravější číslici násobiče. Čte a vymaže tuto číslici.
2. **Podmíněné Sčítání**: Pokud je číslice 1, stroj přičte současný násobenec k akumulátoru. Tento krok odpovídá standardní binární metodě násobení, kde přidáváte násobenec, pokud odpovídající bit násobiče je 1.
3. **Zdvojnásobení Násobence**: Bez ohledu na přečtenou číslici stroj zdvojnásobí násobenec připojením 0. Tato akce odráží posun doleva v binárním násobení (ekvivalentní násobení dvěma).
4. **Posun Násobiče**: Stroj uvolní místo posunutím násobiče o jednu buňku doprava. Tento proces efektivně dělí násobič dvěma a zahazuje nejméně významný bit.
5. **Základní Případ**: Základním případem této rekurzivní operace je, když se násobič stane 0. V tomto bodě proces zastaví a nahromaděná hodnota představuje produkt.
6. **Úpravy Binárního Sčítání**: Stroj zahrnuje úpravy standardního stroje pro binární sčítání, aby udržel symbol '+' a přešel do dalších stavů místo zastavení.
7. **Model Rekurzivní Funkce**: Operace stroje lze chápat jako implementaci rekurzivní funkce `mult(acc, a, b)`, která udržuje invariant `acc + a * b`. Třetí argument `b` (násobič) se vždy snižuje, což zajišťuje, že funkce skončí. Když `b` dosáhne 0, výsledkem je akumulátor, který obsahuje produkt původních `a` a `b`.



