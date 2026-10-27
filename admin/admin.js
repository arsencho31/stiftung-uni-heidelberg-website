/* Autorenpanel: schreibt Artikel (JSON + Bilder) per GitHub-API ins Repository.
   Die Website (GitHub Pages) veröffentlicht die Änderung danach automatisch (ca. 1 Minute).

   Anmeldung mit Login + Passwort ohne eigenen Server:
   admin/accounts.json enthält den GitHub-Token der Website, verschlüsselt mit einem zufälligen
   Hauptschlüssel (AES-GCM). Dieser Hauptschlüssel ist für jeden Login einzeln mit dessen Passwort
   verschlüsselt (PBKDF2-SHA-256, 600 000 Runden). Passwörter werden nirgends gespeichert; sie
   werden im Browser zufällig erzeugt und nur einmal angezeigt. */
(function () {
  "use strict";
  var OWNER = "arsencho31", REPO = "stiftung-uni-heidelberg-website", BRANCH = "main";
  var SITE_URL = "https://" + OWNER + ".github.io/" + REPO + "/";
  var API = "https://api.github.com/repos/" + OWNER + "/" + REPO + "/";
  var ACC = "admin/accounts.json", IDX = "content/articles/index.json", SKEY = "uh-admin";
  var UH = window.UH;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- Oberfläche: Deutsch / Russisch ---------- */
  var S = {
    de: {
      title: "Autorenpanel", logout: "Abmelden", loginTitle: "Anmelden", checking: "Einen Moment …",
      loginIntro: "Für Redakteurinnen und Redakteure der Website.", userLabel: "Login", pwLabel: "Passwort",
      remember: "Auf diesem Gerät angemeldet bleiben", login: "Anmelden",
      forgot: "Passwort vergessen? Bitte an den Inhaber (admin1) wenden.", toSetup: "Ersteinrichtung / Notfallzugang mit GitHub-Token",
      setupTitle: "Ersteinrichtung",
      setupIntro: "Einmalig für den Inhaber der Website: Der GitHub-Zugang wird verschlüsselt hinterlegt, danach erzeugt das Panel Logins mit sicheren Passwörtern. Alle weiteren Personen melden sich nur noch mit Login und Passwort an.",
      setupWarn: "Es gibt bereits Zugänge. Wenn Sie fortfahren, erhalten alle aufgeführten Logins neue Passwörter, und die alten Passwörter funktionieren nicht mehr.",
      howTitle: "So erstellen Sie den GitHub-Token (2 Minuten)", tokenLabel: "GitHub-Token",
      namesLabel: "Logins (durch Komma getrennt; der erste wird Inhaber und verwaltet die Zugänge)", setupBtn: "Zugänge erzeugen", toLogin: "Zur Anmeldung",
      renewTitle: "GitHub-Zugang erneuern", renewIntro: "Der hinterlegte GitHub-Token ist abgelaufen oder wurde widerrufen. Erstellen Sie einen neuen Token und fügen Sie ihn hier ein. Alle Passwörter bleiben gültig.", renewBtn: "Token ersetzen",
      articles: "Artikel", newArticle: "+ Neuer Artikel", back: "← Zurück",
      orderHint: "Reihenfolge wie auf der Website: oben steht zuerst. Zum Verschieben am Griff ⠿ ziehen oder ↑ ↓ benutzen.", sortDate: "Nach Datum sortieren",
      orderDirty: "Neue Reihenfolge ist noch nicht gespeichert.", save: "Speichern", discard: "Verwerfen",
      accountsH: "Zugänge", accountsHint: "Jede Person bekommt einen eigenen Login. Passwörter werden zufällig erzeugt und nur einmal angezeigt.", addUser: "+ Zugang hinzufügen",
      replaceTok: "GitHub-Token ersetzen (z. B. wenn er bald abläuft)", settingsH: "Einstellungen",
      emailLabel: "E-Mail für die automatische Übersetzung (optional – erhöht das kostenlose Tageslimit)",
      credH: "Neue Zugangsdaten", credWarn: "Diese Passwörter werden nur jetzt angezeigt. Speichern Sie sie (z. B. im Passwort-Manager) und geben Sie jeder Person nur ihren eigenen Zugang weiter.",
      copyAll: "Alle kopieren", saveFile: "Als Textdatei speichern", credDone: "Gespeichert – weiter",
      writeIn: "Ich schreibe auf", category: "Erscheint bei", both: "Beiden", date: "Datum",
      "title-field": "Titel", summary: "Kurzfassung (1–2 Sätze, erscheint auf den Karten)", text: "Text", translate: "Jetzt in die andere Sprache übersetzen",
      media: "Fotos und Video", cover: "Titelbild", photos: "Weitere Fotos (mehrere möglich)", videoKind: "Video", none: "Kein Video", videoFile: "Eigene Videodatei (MP4, bis 40 MB)",
      videoUrl: "Link zum Video", videoPick: "MP4-Datei", linksH: "Links", addLink: "+ Link hinzufügen", preview: "Vorschau", publish: "Veröffentlichen (DE + EN)", close: "Schließen",
      // dynamisch
      bad_token: "Token ungültig oder ohne Schreibrecht für dieses Repository.", badLogin: "Login oder Passwort ist falsch.",
      netErr: "Keine Verbindung zu GitHub. Bitte später erneut versuchen.", tokenExpired: "Der GitHub-Zugang der Website ist abgelaufen. Bitte den Inhaber (admin1) informieren.",
      working: "Bitte warten …", badNames: "Logins: nur Kleinbuchstaben, Ziffern, Punkt und Bindestrich (2–32 Zeichen), keine Doppelungen.",
      owner: "Inhaber", editor: "Redaktion", you: "Sie", since: "seit", newPw: "Neues Passwort", exists: "Diesen Login gibt es schon.",
      confirmPw: "Neues Passwort für {u} erzeugen? Das bisherige Passwort funktioniert danach nicht mehr.",
      confirmRm: "Zugang {u} entfernen? Die Person kann sich danach nicht mehr anmelden.",
      copy: "Kopieren", copied: "Kopiert", copyFail: "Kopieren nicht möglich – bitte markieren und kopieren.", panel: "Autorenpanel",
      drag: "Ziehen zum Verschieben", up: "Nach oben", down: "Nach unten", orderSaved: "Reihenfolge gespeichert – auf der Website in ca. 1 Minute.",
      leaveDirty: "Die neue Reihenfolge ist noch nicht gespeichert. Verwerfen?", tokenReplaced: "Token ersetzt. Alle Passwörter bleiben gültig.",
      catStiftung: "Stiftung", catGdf: "Gesellschaft der Freunde", catBoth: "Stiftung + Freunde",
      edit: "Bearbeiten", del: "Löschen", view: "Ansehen", editTitle: "Artikel bearbeiten", noArticles: "Noch keine Artikel.",
      confirmDel: "Diesen Artikel wirklich löschen? (Dauerhaft entfernt.)", needTitle: "Bitte Titel und Text in der gewählten Sprache eingeben.", translating: "Übersetze …", translated: "Übersetzung eingefügt – bitte kurz prüfen.",
      trFail: "Automatische Übersetzung nicht möglich (Limit erreicht oder offline). Bitte Text im anderen Tab selbst eintragen.", trHintSrc: "Sie schreiben auf {l}. Der andere Tab wird beim Veröffentlichen automatisch übersetzt.",
      publishing: "Veröffentliche …", done: "Veröffentlicht! Sichtbar nach ca. 1 Minute: ", remove: "Entfernen", caption: "Bildunterschrift", linkLabel: "Beschriftung", linkUrl: "Adresse (https://…)", tooBig: "Datei zu groß (max. 40 MB).",
      keep: "Aktuelles Video bleibt erhalten, falls Sie nichts Neues wählen.", saving: "Speichere", of: "von"
    },
    ru: {
      title: "Панель автора", logout: "Выйти", loginTitle: "Вход", checking: "Секунду …",
      loginIntro: "Для редакторов сайта.", userLabel: "Логин", pwLabel: "Пароль",
      remember: "Оставаться в системе на этом устройстве", login: "Войти",
      forgot: "Забыли пароль? Обратитесь к владельцу (admin1).", toSetup: "Первичная настройка / аварийный вход по GitHub-токену",
      setupTitle: "Первичная настройка",
      setupIntro: "Один раз для владельца сайта: доступ к GitHub сохраняется в зашифрованном виде, затем панель создаёт логины с надёжными паролями. Все остальные входят только по логину и паролю.",
      setupWarn: "Аккаунты уже существуют. Если продолжить, все перечисленные логины получат новые пароли, а старые перестанут работать.",
      howTitle: "Как создать GitHub-токен (2 минуты)", tokenLabel: "GitHub-токен",
      namesLabel: "Логины через запятую (первый становится владельцем и управляет аккаунтами)", setupBtn: "Создать аккаунты", toLogin: "К входу",
      renewTitle: "Обновить доступ к GitHub", renewIntro: "Сохранённый GitHub-токен истёк или был отозван. Создайте новый токен и вставьте его сюда. Все пароли останутся прежними.", renewBtn: "Заменить токен",
      articles: "Статьи", newArticle: "+ Новая статья", back: "← Назад",
      orderHint: "Порядок как на сайте: сверху — первая. Перетаскивайте за ⠿ или используйте ↑ ↓.", sortDate: "Сортировать по дате",
      orderDirty: "Новый порядок ещё не сохранён.", save: "Сохранить", discard: "Отменить",
      accountsH: "Аккаунты", accountsHint: "У каждого человека свой логин. Пароли генерируются случайно и показываются только один раз.", addUser: "+ Добавить аккаунт",
      replaceTok: "Заменить GitHub-токен (например, перед истечением срока)", settingsH: "Настройки",
      emailLabel: "E-mail для автоперевода (необязательно — увеличивает бесплатный дневной лимит)",
      credH: "Новые данные для входа", credWarn: "Эти пароли показываются только сейчас. Сохраните их (например, в менеджере паролей) и передавайте каждому только его собственный доступ.",
      copyAll: "Скопировать всё", saveFile: "Сохранить в текстовый файл", credDone: "Сохранил — дальше",
      writeIn: "Пишу на языке", category: "Показывать у", both: "Обоих", date: "Дата",
      "title-field": "Заголовок", summary: "Краткое описание (1–2 предложения, для карточек)", text: "Текст", translate: "Перевести сейчас на другой язык",
      media: "Фото и видео", cover: "Главное фото", photos: "Дополнительные фото (можно несколько)", videoKind: "Видео", none: "Без видео", videoFile: "Свой видеофайл (MP4, до 40 МБ)",
      videoUrl: "Ссылка на видео", videoPick: "Файл MP4", linksH: "Ссылки", addLink: "+ Добавить ссылку", preview: "Предпросмотр", publish: "Опубликовать (DE + EN)", close: "Закрыть",
      bad_token: "Токен недействителен или нет права записи в этот репозиторий.", badLogin: "Неверный логин или пароль.",
      netErr: "Нет связи с GitHub. Попробуйте позже.", tokenExpired: "Доступ сайта к GitHub истёк. Сообщите владельцу (admin1).",
      working: "Подождите …", badNames: "Логины: только строчные латинские буквы, цифры, точка и дефис (2–32 символа), без повторов.",
      owner: "Владелец", editor: "Редактор", you: "Вы", since: "с", newPw: "Новый пароль", exists: "Такой логин уже есть.",
      confirmPw: "Создать новый пароль для {u}? Старый пароль перестанет работать.",
      confirmRm: "Удалить аккаунт {u}? Этот человек больше не сможет войти.",
      copy: "Копировать", copied: "Скопировано", copyFail: "Не удалось скопировать — выделите и скопируйте вручную.", panel: "Панель автора",
      drag: "Перетащите, чтобы переместить", up: "Выше", down: "Ниже", orderSaved: "Порядок сохранён — на сайте примерно через минуту.",
      leaveDirty: "Новый порядок ещё не сохранён. Отменить его?", tokenReplaced: "Токен заменён. Все пароли остались прежними.",
      catStiftung: "Фонд", catGdf: "Общество друзей", catBoth: "Фонд + Общество",
      edit: "Изменить", del: "Удалить", view: "Открыть", editTitle: "Редактирование статьи", noArticles: "Статей пока нет.",
      confirmDel: "Удалить статью насовсем?", needTitle: "Введите заголовок и текст на выбранном языке.", translating: "Перевожу …", translated: "Перевод вставлен — коротко проверьте.",
      trFail: "Автоперевод недоступен (лимит или нет сети). Заполните второй язык вручную.", trHintSrc: "Вы пишете на языке: {l}. Вторая вкладка переведётся автоматически при публикации.",
      publishing: "Публикую …", done: "Опубликовано! Появится на сайте примерно через минуту: ", remove: "Убрать", caption: "Подпись к фото", linkLabel: "Название", linkUrl: "Адрес (https://…)", tooBig: "Файл слишком большой (макс. 40 МБ).",
      keep: "Текущее видео сохранится, если не выбрать новое.", saving: "Сохраняю", of: "из"
    }
  };
  var HTMLK = {
    de: {
      how1: 'Bei GitHub anmelden und <a href="https://github.com/settings/personal-access-tokens/new" target="_blank" rel="noopener">github.com/settings/personal-access-tokens/new</a> öffnen.',
      how2: 'Name z. B. <code>Autorenpanel</code>; „Expiration“: so lange wie möglich (das Panel erinnert, wenn er abläuft).',
      how3: '„Repository access“: <b>Only select repositories</b> wählen und unter „Select repositories“ <code>stiftung-uni-heidelberg-website</code> auswählen.',
      how4: '„Permissions“: Reiter <b>Repositories</b> → „Add permissions“ → <b>Contents</b> anhaken → daneben „Read-only“ auf <b>Read and write</b> umstellen. Der Reiter erscheint erst nach Schritt 3.',
      how5: '„Generate token“ klicken und den Token (beginnt mit <code>github_pat_</code>) hier einfügen. Er wird nur verschlüsselt gespeichert.',
      mdHelp: 'Formatierung: <code>## Zwischenüberschrift</code>, <code>- Listenpunkt</code>, <code>**fett**</code>, <code>*kursiv*</code>, <code>[Linktext](https://…)</code>. Leerzeile = neuer Absatz.'
    },
    ru: {
      how1: 'Войдите в GitHub и откройте <a href="https://github.com/settings/personal-access-tokens/new" target="_blank" rel="noopener">github.com/settings/personal-access-tokens/new</a>.',
      how2: 'Имя, например, <code>Autorenpanel</code>; «Expiration» — максимально долгий срок (панель подскажет, когда он истечёт).',
      how3: '«Repository access»: выберите <b>Only select repositories</b> и в «Select repositories» отметьте <code>stiftung-uni-heidelberg-website</code>.',
      how4: '«Permissions»: вкладка <b>Repositories</b> → «Add permissions» → отметьте <b>Contents</b> → рядом переключите «Read-only» на <b>Read and write</b>. Вкладка появляется только после шага 3.',
      how5: 'Нажмите «Generate token» и вставьте токен (начинается с <code>github_pat_</code>) сюда. Он сохраняется только в зашифрованном виде.',
      mdHelp: 'Форматирование: <code>## Подзаголовок</code>, <code>- пункт списка</code>, <code>**жирный**</code>, <code>*курсив*</code>, <code>[текст ссылки](https://…)</code>. Пустая строка = новый абзац.'
    }
  };
  var ui = localStorage.getItem("uh-admin-ui") || "de";
  function t(k) { return (S[ui] && S[ui][k]) || S.de[k] || k; }
  function applyUi() {
    $$("[data-i]").forEach(function (el) {
      var k = el.getAttribute("data-i"), v = (S[ui] && S[ui][k]);
      if (HTMLK[ui][k]) { el.innerHTML = HTMLK[ui][k]; return; }
      if (v == null) return;
      if (el.tagName === "OPTION" || el.children.length === 0) el.textContent = v;
      else if (k === "title") el.textContent = v;
    });
    // einzelne Beschriftungen mit Unterstruktur
    $$("label > span[data-i='title']").forEach(function (e) { e.textContent = t("title-field"); });
    $("#uiLang span").textContent = ui === "de" ? "RU" : "DE";
    document.documentElement.lang = ui;
    updateHint();
    if (!$("#list").hidden) { drawList(); if (accUsers) drawAccounts(accUsers); }
  }

  /* ---------- Sitzung ---------- */
  ["uh-token"].forEach(function (k) { localStorage.removeItem(k); sessionStorage.removeItem(k); }); // früherer Token-Login
  function readSess() { try { return JSON.parse(sessionStorage.getItem(SKEY) || localStorage.getItem(SKEY) || "null"); } catch (e) { return null; } }
  var sess = readSess(), remember = !!localStorage.getItem(SKEY);
  function clearStore() { localStorage.removeItem(SKEY); sessionStorage.removeItem(SKEY); }
  function storeSess() { clearStore(); (remember ? localStorage : sessionStorage).setItem(SKEY, JSON.stringify(sess)); }
  function by(msg) { return msg + (sess && sess.user ? " [" + sess.user + "]" : ""); }

  /* ---------- GitHub-API ---------- */
  function gh(path, opts) {
    opts = opts || {};
    opts.headers = Object.assign({ Authorization: "Bearer " + (opts.tok || (sess && sess.token) || ""), Accept: "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28" }, opts.headers || {});
    return fetch(API + path, opts).then(function (r) {
      if (r.status === 404 && opts.allow404) return null;
      if (!r.ok) return r.json().catch(function () { return {}; }).then(function (j) { var e = new Error(j.message || r.status); e.status = r.status; throw e; });
      return r.status === 204 ? {} : r.json();
    });
  }
  function b64enc(str) { var b = new TextEncoder().encode(str), s = ""; b.forEach(function (c) { s += String.fromCharCode(c); }); return btoa(s); }
  function b64dec(b64) { var s = atob(b64.replace(/\n/g, "")), a = new Uint8Array(s.length); for (var i = 0; i < s.length; i++) a[i] = s.charCodeAt(i); return new TextDecoder().decode(a); }
  function enc(path) { return path.split("/").map(encodeURIComponent).join("/"); }
  function getFile(path) { return gh("contents/" + enc(path) + "?ref=" + BRANCH, { allow404: true }); }
  function putFile(path, b64, msg, sha) {
    var body = { message: msg, content: b64, branch: BRANCH }; if (sha) body.sha = sha;
    return gh("contents/" + enc(path), { method: "PUT", body: JSON.stringify(body) });
  }
  function delFile(path, sha, msg) { return gh("contents/" + enc(path), { method: "DELETE", body: JSON.stringify({ message: msg, sha: sha, branch: BRANCH }) }); }
  function readJSON(path) { return getFile(path).then(function (f) { return f ? { sha: f.sha, data: JSON.parse(b64dec(f.content)) } : null; }); }
  function checkRepo(tok) {
    return gh("", { tok: tok }).then(function (repo) {
      if (!repo.permissions || !repo.permissions.push) { var e = new Error(t("bad_token")); e.status = 403; throw e; }
    });
  }

  /* ---------- Verschlüsselung (Web Crypto) ---------- */
  var ITER = 600000, te = new TextEncoder(), td = new TextDecoder();
  function u8b64(u8) { var s = ""; for (var i = 0; i < u8.length; i++) s += String.fromCharCode(u8[i]); return btoa(s); }
  function b64u8(b) { var s = atob(b), a = new Uint8Array(s.length); for (var i = 0; i < s.length; i++) a[i] = s.charCodeAt(i); return a; }
  function rand(n) { return crypto.getRandomValues(new Uint8Array(n)); }
  function pwKey(pw, salt, iter) {
    return crypto.subtle.importKey("raw", te.encode(pw), "PBKDF2", false, ["deriveKey"]).then(function (k) {
      return crypto.subtle.deriveKey({ name: "PBKDF2", hash: "SHA-256", salt: salt, iterations: iter }, k, { name: "AES-GCM", length: 256 }, false, ["encrypt", "decrypt"]);
    });
  }
  function aesKey(raw) { return crypto.subtle.importKey("raw", raw, "AES-GCM", false, ["encrypt", "decrypt"]); }
  function seal(key, bytes) { var iv = rand(12); return crypto.subtle.encrypt({ name: "AES-GCM", iv: iv }, key, bytes).then(function (ct) { return { iv: u8b64(iv), ct: u8b64(new Uint8Array(ct)) }; }); }
  function unseal(key, box) { return crypto.subtle.decrypt({ name: "AES-GCM", iv: b64u8(box.iv) }, key, b64u8(box.ct)).then(function (b) { return new Uint8Array(b); }); }
  function sealToken(mkRaw, tok) { return aesKey(mkRaw).then(function (mk) { return seal(mk, te.encode(JSON.stringify({ token: tok }))); }); }
  function wrapFor(pw, mkRaw) {
    var salt = rand(16);
    return pwKey(pw, salt, ITER).then(function (k) { return seal(k, mkRaw); }).then(function (b) { return { salt: u8b64(salt), iter: ITER, iv: b.iv, key: b.ct }; });
  }
  // 20 Zeichen aus 56 gut unterscheidbaren Zeichen (≈ 116 Bit), gleichverteilt, in Fünfergruppen
  function genPassword() {
    var A = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789", out = "";
    while (out.length < 20) { var b = rand(32); for (var i = 0; i < b.length && out.length < 20; i++) if (b[i] < 224) out += A[b[i] % 56]; }
    return out.match(/.{5}/g).join("-");
  }
  function unlock(acc, user, pw) {
    var u = acc && acc.users && Object.prototype.hasOwnProperty.call(acc.users, user) && acc.users[user], mkRaw;
    if (!u) return Promise.reject(new Error(t("badLogin")));
    return pwKey(pw, b64u8(u.salt), u.iter || ITER).then(function (k) { return unseal(k, { iv: u.iv, ct: u.key }); })
      .catch(function () { throw new Error(t("badLogin")); })
      .then(function (raw) { mkRaw = raw; return aesKey(raw); })
      .then(function (mk) { return unseal(mk, acc.vault); })
      .then(function (p) {
        var v = JSON.parse(td.decode(p)), owner = u.role === "owner";
        return { user: user, role: owner ? "owner" : "editor", token: v.token, mk: owner ? u8b64(mkRaw) : null };
      });
  }

  /* ---------- Zugänge (admin/accounts.json) ---------- */
  var accCache = null, accUsers = null;
  // ohne Anmeldung lesbar: öffentliche API, ersatzweise die veröffentlichte Datei
  function fetchAccounts() {
    return fetch(API + "contents/" + ACC + "?ref=" + BRANCH, { headers: { Accept: "application/vnd.github.raw+json" }, cache: "no-store" })
      .then(function (r) { if (r.status === 404) return null; if (!r.ok) throw new Error(r.status); return r.json(); })
      .catch(function (e) {
        return fetch("accounts.json?t=" + Date.now(), { cache: "no-store" }).then(function (r) { if (r.status === 404) return null; if (!r.ok) throw e; return r.json(); });
      })
      .then(function (acc) { accCache = acc; return acc; });
  }
  function saveAccounts(fn, msg) {
    return readJSON(ACC).then(function (r) {
      var acc = fn(r ? r.data : null);
      return putFile(ACC, b64enc(JSON.stringify(acc, null, 1)), by(msg), r && r.sha).then(function () { return acc; });
    });
  }
  function parseNames(s) {
    var arr = String(s).toLowerCase().split(/[\s,;]+/).filter(Boolean), seen = {};
    if (!arr.length || arr.length > 20) throw new Error(t("badNames"));
    arr.forEach(function (n) { if (!/^[a-z0-9][a-z0-9._-]{1,31}$/.test(n) || seen[n]) throw new Error(t("badNames")); seen[n] = 1; });
    return arr;
  }
  function credLine(c) { return t("panel") + ": " + SITE_URL + "admin/\n" + t("userLabel") + ": " + c[0] + "\n" + t("pwLabel") + ": " + c[1]; }
  function copy(txt) { (navigator.clipboard ? navigator.clipboard.writeText(txt) : Promise.reject()).then(function () { UH.toast(t("copied")); }, function () { UH.toast(t("copyFail")); }); }
  var credText = "", credAfter = null;
  function showCreds(list, after) {
    credText = list.map(credLine).join("\n\n"); credAfter = after || null;
    var box = $("#credRows"); box.innerHTML = "";
    list.forEach(function (c) {
      var d = document.createElement("div"); d.className = "cred";
      d.innerHTML = '<b></b><code></code><button type="button" class="btn ghost sm">' + t("copy") + "</button>";
      $("b", d).textContent = c[0]; $("code", d).textContent = c[1];
      $("button", d).onclick = function () { copy(credLine(c)); };
      box.appendChild(d);
    });
    $("#credModal").hidden = false; $("#credDone").focus();
  }
  $("#credCopy").onclick = function () { copy(credText); };
  $("#credSave").onclick = function () {
    var a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([credText + "\n"], { type: "text/plain;charset=utf-8" })); a.download = "zugaenge-autorenpanel.txt";
    document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
  };
  $("#credDone").onclick = function () {
    $("#credModal").hidden = true; $("#credRows").innerHTML = ""; credText = "";
    var f = credAfter; credAfter = null; if (f) f();
  };

  // Verwaltung (nur Inhaber; braucht den Hauptschlüssel aus der Sitzung)
  function loadAccounts() {
    var owner = sess && sess.role === "owner" && sess.mk;
    $("#accounts").hidden = !owner; if (!owner) return;
    readJSON(ACC).then(function (r) { drawAccounts(r ? r.data.users : {}); }, function (e) { $("#accErr").textContent = e.message; });
  }
  function drawAccounts(users) {
    accUsers = users || {};
    var box = $("#accRows"), names = Object.keys(accUsers); box.innerHTML = "";
    names.forEach(function (n) {
      var u = accUsers[n], d = document.createElement("div"); d.className = "acc-row";
      d.innerHTML = '<b></b><span class="role"></span><span class="since"></span><button type="button" class="btn ghost sm" data-r>' + t("newPw") + "</button>" +
        (n === sess.user ? "" : '<button type="button" class="btn danger sm" data-x>' + t("remove") + "</button>");
      $("b", d).textContent = n;
      $(".role", d).textContent = u.role === "owner" ? t("owner") : t("editor"); if (u.role === "owner") $(".role", d).classList.add("owner");
      $(".since", d).textContent = (n === sess.user ? t("you") + " · " : "") + (u.created ? t("since") + " " + u.created : "");
      $("[data-r]", d).onclick = function () { if (confirm(t("confirmPw").replace("{u}", n))) accJob(setPw(n)); };
      var x = $("[data-x]", d); if (x) x.onclick = function () { if (confirm(t("confirmRm").replace("{u}", n))) accJob(removeUser(n)); };
      box.appendChild(d);
    });
    for (var i = 1; names.indexOf("admin" + i) > -1; i++);
    $("#newName").placeholder = "admin" + i;
  }
  function accJob(p) {
    $("#accErr").textContent = ""; $$("#accounts button").forEach(function (b) { b.disabled = true; });
    return p.then(function (creds) { if (creds) showCreds([creds]); }, function (e) { $("#accErr").textContent = e.message; })
      .then(function () { $$("#accounts button").forEach(function (b) { b.disabled = false; }); loadAccounts(); });
  }
  // neues Passwort für bestehenden oder neuen Login; gibt [login, passwort] zurück
  function setPw(name, isNew) {
    var pw = genPassword();
    return wrapFor(pw, b64u8(sess.mk)).then(function (w) {
      return saveAccounts(function (acc) {
        var old = acc.users[name];
        if (isNew && old) throw new Error(t("exists"));
        w.role = (old && old.role) || "editor"; w.created = (old && old.created) || today(); if (old) w.changed = today();
        acc.users[name] = w; return acc;
      }, (isNew ? "Zugang hinzugefügt: " : "Neues Passwort für ") + name);
    }).then(function () { return [name, pw]; });
  }
  function removeUser(name) {
    return saveAccounts(function (acc) { if (name !== sess.user) delete acc.users[name]; return acc; }, "Zugang entfernt: " + name).then(function () { return null; });
  }
  function replaceToken(tok) {
    return checkRepo(tok).then(function () { return sealToken(b64u8(sess.mk), tok); }).then(function (vault) {
      sess.token = tok;
      return saveAccounts(function (acc) { acc.vault = vault; return acc; }, "GitHub-Zugang des Autorenpanels erneuert");
    }).then(function () { storeSess(); });
  }
  $("#addForm").onsubmit = function (ev) {
    ev.preventDefault();
    var n; try { n = parseNames($("#newName").value.trim() || $("#newName").placeholder); } catch (e) { $("#accErr").textContent = e.message; return; }
    accJob(setPw(n[0], true)).then(function () { $("#newName").value = ""; });
  };
  $("#replaceForm").onsubmit = function (ev) {
    ev.preventDefault(); var tok = $("#replaceToken").value.trim(); if (!tok) return;
    accJob(replaceToken(tok).then(function () { $("#replaceToken").value = ""; UH.toast(t("tokenReplaced")); }));
  };

  /* ---------- Hilfsfunktionen ---------- */
  var SECTIONS = ["boot", "login", "setup", "renew", "list", "editor"];
  function show(id) {
    SECTIONS.forEach(function (s) { $("#" + s).hidden = s !== id; });
    var inside = !!sess && ["list", "editor", "renew"].indexOf(id) > -1;
    $("#logout").hidden = !inside; $("#who").hidden = !inside; if (sess) $("#who").textContent = sess.user;
    window.scrollTo(0, 0);
  }
  function slugify(s) {
    var map = { "ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "sch", "ы": "y", "э": "e", "ю": "yu", "я": "ya" };
    return String(s).toLowerCase().replace(/./g, function (c) { return map[c] != null ? map[c] : c; }).normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 55);
  }
  function fileToDataUrl(file) { return new Promise(function (res, rej) { var r = new FileReader(); r.onload = function () { res(r.result); }; r.onerror = rej; r.readAsDataURL(file); }); }
  function shrinkImage(file, max) {
    return fileToDataUrl(file).then(function (url) {
      return new Promise(function (res, rej) {
        var img = new Image();
        img.onload = function () {
          var k = Math.min(1, max / Math.max(img.width, img.height)), c = document.createElement("canvas");
          c.width = Math.round(img.width * k); c.height = Math.round(img.height * k);
          var g = c.getContext("2d"); g.fillStyle = "#fff"; g.fillRect(0, 0, c.width, c.height); g.drawImage(img, 0, 0, c.width, c.height);
          res(c.toDataURL("image/jpeg", 0.86));
        };
        img.onerror = rej; img.src = url;
      });
    });
  }
  function dataUrlB64(u) { return u.split(",")[1]; }
  function today() { var d = new Date(); return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"); }
  function shortDate(d) { var x = new Date(d + "T12:00:00"); return isNaN(x) ? d : x.toLocaleDateString(ui === "ru" ? "ru-RU" : "de-DE", { day: "numeric", month: "short", year: "numeric" }); }
  function catName(c) { return t(c === "gdf" ? "catGdf" : c === "both" ? "catBoth" : "catStiftung"); }

  /* ---------- Übersetzung (MyMemory, kostenlos, ohne Schlüssel) ---------- */
  var email = localStorage.getItem("uh-email") || "";
  var trCache = {};
  function trChunk(text, from, to) {
    var key = from + to + text; if (trCache[key]) return Promise.resolve(trCache[key]);
    var url = "https://api.mymemory.translated.net/get?q=" + encodeURIComponent(text) + "&langpair=" + from + "|" + to + (email ? "&de=" + encodeURIComponent(email) : "");
    return fetch(url).then(function (r) { return r.json(); }).then(function (j) {
      var out = j && j.responseData && j.responseData.translatedText;
      if (!out || j.responseStatus !== 200 || /MYMEMORY WARNING|QUERY LENGTH LIMIT/i.test(out)) throw new Error("translate");
      out = out.replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, "&"); trCache[key] = out; return out;
    });
  }
  function trPlain(text, from, to) {
    if (!/[A-Za-zÀ-ÿА-я]/.test(text)) return Promise.resolve(text);
    var lead = (text.match(/^\s*/) || [""])[0], trail = (text.match(/\s*$/) || [""])[0], core = text.trim();
    var parts = core.match(/[^.!?]+[.!?]*\s*/g) || [core], chunks = [], cur = "";
    parts.forEach(function (p) { if ((cur + p).length > 420 && cur) { chunks.push(cur); cur = p; } else cur += p; }); if (cur) chunks.push(cur);
    return chunks.reduce(function (pr, c) { return pr.then(function (acc) { return trChunk(c.trim(), from, to).then(function (o) { return acc.concat(o); }); }); }, Promise.resolve([]))
      .then(function (arr) { return lead + arr.join(" ") + trail; });
  }
  function trInline(line, from, to) {
    // Links: Adresse durch Platzhalter ersetzen, ganze Zeile übersetzen (Markierungen bleiben so im Satzzusammenhang), Adressen zurücksetzen
    var urls = [], safe = line.replace(/\]\(([^)\s]+)\)/g, function (m, u) { urls.push(u); return "](§" + urls.length + "§)"; });
    return trPlain(safe, from, to).then(function (o) {
      o = o.replace(/\(\s*§\s*(\d+)\s*§\s*\)/g, function (m, n) { return "(" + (urls[n - 1] || "") + ")"; });
      var bad = (o.match(/\*\*/g) || []).length % 2 || /§\d+§/.test(o);
      return bad ? o.replace(/\*+/g, "").replace(/\[([^\]]*)\]\(§?\d*§?\)/g, "$1") : o;
    });
  }
  function trMarkdown(src, from, to) {
    var lines = String(src || "").replace(/\r/g, "").split("\n");
    return lines.reduce(function (pr, ln) {
      return pr.then(function (acc) {
        if (!ln.trim()) return acc.concat("");
        var m = ln.match(/^(#{2,3}\s+|[-*]\s+)(.*)$/), pre = m ? m[1] : "", rest = m ? m[2] : ln;
        return trInline(rest, from, to).then(function (o) { return acc.concat(pre + o); });
      });
    }, Promise.resolve([])).then(function (a) { return a.join("\n"); });
  }
  function trShort(s, from, to) { return s && s.trim() ? trInline(s, from, to) : Promise.resolve(""); }

  /* ---------- Editor-Zustand ---------- */
  var state = { id: null, sha: null, existing: null, cover: null, photos: [], videoExisting: null, videoNewFile: null, links: [] };
  var curTab = "de";
  function srcLang() { return $("#srcLang").value; }
  function otherLang() { return srcLang() === "de" ? "en" : "de"; }
  function val(id) { return $("#" + id).value; }
  function langName(l) { return l === "de" ? "Deutsch" : "English"; }
  function updateHint() { $("#trHint").textContent = t("trHintSrc").replace("{l}", langName(srcLang())); }

  function setTab(l) {
    curTab = l;
    ["de", "en"].forEach(function (x) { $("#pane-" + x).hidden = x !== l; $("#tab-" + x).setAttribute("aria-selected", x === l); });
  }
  $("#tab-de").onclick = function () { setTab("de"); }; $("#tab-en").onclick = function () { setTab("en"); };
  $("#srcLang").onchange = function () { setTab(srcLang()); updateHint(); };

  // Werkzeugleiste (fett, kursiv, Überschrift, Liste, Link)
  $$(".toolbar").forEach(function (tb) {
    var ta = $("#" + tb.getAttribute("data-for"));
    function wrap(a, b, ph) { var s = ta.selectionStart, e = ta.selectionEnd, sel = ta.value.slice(s, e) || ph; ta.setRangeText(a + sel + b, s, e, "end"); ta.focus(); }
    function line(prefix) { var s = ta.selectionStart; var ls = ta.value.lastIndexOf("\n", s - 1) + 1; ta.setRangeText(prefix, ls, ls, "end"); ta.focus(); }
    [["B", function () { wrap("**", "**", "fett"); }], ["I", function () { wrap("*", "*", "kursiv"); }], ["H2", function () { line("## "); }], ["•", function () { line("- "); }],
     ["🔗", function () { var u = prompt("https://…"); if (u) wrap("[", "](" + u + ")", "Link"); }]].forEach(function (b) {
      var btn = document.createElement("button"); btn.type = "button"; btn.textContent = b[0]; btn.onclick = b[1]; tb.appendChild(btn);
    });
  });

  // Video-Auswahl
  function syncVideo() {
    var k = $("#videoKind").value;
    $("#videoUrlWrap").hidden = !(k === "youtube" || k === "vimeo"); $("#videoFileWrap").hidden = k !== "file";
    $("#videoCur").textContent = (k === "file" && state.videoExisting && state.videoExisting.kind === "file") ? t("keep") : "";
  }
  $("#videoKind").onchange = syncVideo;
  $("#videoFile").onchange = function () { var f = this.files[0]; if (f && f.size > 40 * 1024 * 1024) { alert(t("tooBig")); this.value = ""; state.videoNewFile = null; } else state.videoNewFile = f || null; };

  // Titelbild & Fotos
  $("#coverFile").onchange = function () {
    var f = this.files[0]; if (!f) return;
    shrinkImage(f, 1600).then(function (u) { state.cover = { dataUrl: u }; renderCover(); });
  };
  function renderCover() {
    var src = state.cover ? (state.cover.dataUrl || UH.asset(state.cover.path)) : "";
    $("#coverPrev").innerHTML = src ? '<img alt="" src="' + UH.esc(src) + '"> <button type="button" class="x" id="rmCover">' + t("remove") + "</button>" : "";
    var rm = $("#rmCover"); if (rm) rm.onclick = function () { state.cover = null; $("#coverFile").value = ""; renderCover(); };
  }
  $("#photoFiles").onchange = function () {
    var files = Array.prototype.slice.call(this.files), self = this;
    files.reduce(function (pr, f) { return pr.then(function () { return shrinkImage(f, 1600).then(function (u) { state.photos.push({ dataUrl: u, cap: "" }); }); }); }, Promise.resolve()).then(function () { self.value = ""; renderPhotos(); });
  };
  function renderPhotos() {
    var box = $("#photoList"); box.innerHTML = "";
    state.photos.forEach(function (p, i) {
      var d = document.createElement("div"); d.className = "photo-item";
      d.innerHTML = '<img alt="" src="' + UH.esc(p.dataUrl || UH.asset(p.path)) + '"><label><span>' + t("caption") + "</span><input></label><button type=\"button\" class=\"x\">" + t("remove") + "</button>";
      $("input", d).value = p.cap || ""; $("input", d).oninput = function () { p.cap = this.value; };
      $(".x", d).onclick = function () { state.photos.splice(i, 1); renderPhotos(); };
      box.appendChild(d);
    });
  }
  // Links
  function renderLinks() {
    var box = $("#linkRows"); box.innerHTML = "";
    state.links.forEach(function (l, i) {
      var d = document.createElement("div"); d.className = "link-row";
      d.innerHTML = "<label><span>" + t("linkLabel") + "</span><input></label><label><span>" + t("linkUrl") + '</span><input type="url"></label><button type="button" class="x">' + t("remove") + "</button>";
      var ins = $$("input", d); ins[0].value = l.label || ""; ins[1].value = l.url || "";
      ins[0].oninput = function () { l.label = this.value; }; ins[1].oninput = function () { l.url = this.value; };
      $(".x", d).onclick = function () { state.links.splice(i, 1); renderLinks(); };
      box.appendChild(d);
    });
  }
  $("#addLink").onclick = function () { state.links.push({ label: "", url: "" }); renderLinks(); };

  function resetEditor() {
    state = { id: null, sha: null, existing: null, cover: null, photos: [], videoExisting: null, videoNewFile: null, links: [] };
    ["title-de", "summary-de", "body-de", "title-en", "summary-en", "body-en", "videoUrl"].forEach(function (i) { $("#" + i).value = ""; });
    $("#date").value = today(); $("#category").value = "stiftung"; $("#srcLang").value = "de"; $("#videoKind").value = "";
    $("#coverFile").value = ""; $("#photoFiles").value = ""; $("#videoFile").value = "";
    $("#trStatus").textContent = ""; $("#pubStatus").textContent = ""; $("#pubStatus").className = "muted";
    renderCover(); renderPhotos(); renderLinks(); syncVideo(); setTab("de"); updateHint();
  }

  /* ---------- Artikelliste und Reihenfolge ---------- */
  var list = [], saved = [], dragFrom = null;   // angezeigte bzw. zuletzt gespeicherte Reihenfolge
  function ids(arr) { return arr.map(function (a) { return a.id; }).join("|"); }
  function dirty() { return ids(list) !== ids(saved); }
  function leaveOk() { return !dirty() || confirm(t("leaveDirty")); }
  function loadList() {
    show("list"); $("#rows").innerHTML = '<li class="muted">…</li>'; loadAccounts();
    return readJSON(IDX).then(function (r) { saved = r ? (r.data.articles || []) : []; list = saved.slice(); drawList(); },
      function (e) { $("#rows").innerHTML = '<li class="err">' + UH.esc(e.message) + "</li>"; });
  }
  function move(from, to, focusSel) {
    if (from == null || to < 0 || to >= list.length || from === to) return;
    list.splice(to, 0, list.splice(from, 1)[0]); drawList();
    var f = focusSel && $("#rows").children[to] && $(focusSel, $("#rows").children[to]); if (f && !f.disabled) f.focus();
  }
  function clearDrop() { $$(".drop-before,.drop-after").forEach(function (e) { e.classList.remove("drop-before", "drop-after"); }); }
  function drawList() {
    var box = $("#rows"), was = {}; box.innerHTML = "";
    saved.forEach(function (a, i) { was[a.id] = i; });
    if (!list.length) box.innerHTML = '<li class="empty">' + t("noArticles") + "</li>";
    list.forEach(function (a, i) {
      var li = document.createElement("li"), ti = (a.de && a.de.title) || (a.en && a.en.title) || a.id;
      li.className = "art-row" + (was[a.id] !== i ? " moved" : ""); li.draggable = true;
      li.innerHTML = '<span class="grip" title="' + t("drag") + '" aria-hidden="true">⠿</span><span class="pos">' + (i + 1) + "</span>" +
        (a.cover ? '<img class="thumb" alt="" loading="lazy" draggable="false" onerror="this.style.visibility=\'hidden\'" src="' + UH.esc(UH.asset(a.cover)) + '">' : '<span class="thumb"></span>') +
        "<div><b>" + UH.esc(ti) + '</b><span class="meta">' + UH.esc(shortDate(a.date)) + " · " + UH.esc(catName(a.category)) + "</span></div>" +
        '<div class="btns"><button type="button" class="mv" data-up title="' + t("up") + '" aria-label="' + t("up") + '"' + (i ? "" : " disabled") + ">↑</button>" +
        '<button type="button" class="mv" data-down title="' + t("down") + '" aria-label="' + t("down") + '"' + (i < list.length - 1 ? "" : " disabled") + ">↓</button>" +
        '<a class="btn ghost sm" target="_blank" rel="noopener" href="' + SITE_URL + "artikel.html?id=" + encodeURIComponent(a.id) + '">' + t("view") + "</a>" +
        '<button class="btn sm" type="button" data-e>' + t("edit") + '</button><button class="btn danger sm" type="button" data-d>' + t("del") + "</button></div>";
      $("[data-up]", li).onclick = function () { move(i, i - 1, "[data-up]"); };
      $("[data-down]", li).onclick = function () { move(i, i + 1, "[data-down]"); };
      $("[data-e]", li).onclick = function () { if (leaveOk()) openEditor(a.id); };
      $("[data-d]", li).onclick = function () { if (leaveOk() && confirm(t("confirmDel"))) deleteArticle(a.id).then(loadList, function (e) { alert(e.message); }); };
      // Ziehen und Ablegen (Maus); auf Touch-Geräten die Pfeile
      li.addEventListener("dragstart", function (e) { dragFrom = i; li.classList.add("dragging"); e.dataTransfer.effectAllowed = "move"; e.dataTransfer.setData("text/plain", a.id); });
      li.addEventListener("dragend", function () { dragFrom = null; li.classList.remove("dragging"); clearDrop(); });
      li.addEventListener("dragover", function (e) {
        if (dragFrom == null) return; e.preventDefault();
        var r = li.getBoundingClientRect(); clearDrop(); li.classList.add(e.clientY > r.top + r.height / 2 ? "drop-after" : "drop-before");
      });
      li.addEventListener("drop", function (e) {
        e.preventDefault(); if (dragFrom == null) return;
        var r = li.getBoundingClientRect(), to = i + (e.clientY > r.top + r.height / 2 ? 1 : 0), from = dragFrom;
        if (from < to) to--; dragFrom = null; move(from, to);
      });
      box.appendChild(li);
    });
    $("#orderBar").hidden = !dirty();
  }
  $("#sortDate").onclick = function () { list.sort(function (a, b) { return a.date < b.date ? 1 : a.date > b.date ? -1 : 0; }); drawList(); };
  $("#orderUndo").onclick = function () { list = saved.slice(); drawList(); };
  $("#orderSave").onclick = function () {
    var btn = this, order = list.map(function (a) { return a.id; }); btn.disabled = true;
    updateIndex(function (arr) { return applyOrder(arr, order); }, "Reihenfolge der Artikel geändert")
      .then(function () { UH.toast(t("orderSaved")); return loadList(); }, function (e) { alert(e.message); })
      .then(function () { btn.disabled = false; });
  };
  function newArticle() { resetEditor(); $("#edTitle").textContent = t("newArticle").replace(/^\+\s*/, ""); show("editor"); }
  $("#newBtn").onclick = function () { if (leaveOk()) newArticle(); };
  $("#cancelBtn").onclick = loadList;

  function openEditor(id) {
    return readJSON("content/articles/" + id + ".json").then(function (r) {
      if (!r) return loadList(); var a = r.data; resetEditor(); state.id = a.id; state.sha = r.sha; state.existing = a;
      $("#edTitle").textContent = t("editTitle");
      ["de", "en"].forEach(function (l) { var c = a[l] || {}; $("#title-" + l).value = c.title || ""; $("#summary-" + l).value = c.summary || ""; $("#body-" + l).value = c.body || ""; });
      $("#date").value = a.date; $("#category").value = a.category;
      state.cover = a.cover ? { path: a.cover } : null;
      state.photos = (a.images || []).map(function (im) { return { path: im.src, cap: im.de || im.en || "", capDe: im.de, capEn: im.en }; });
      state.links = (a.links || []).map(function (l) { return { url: l.url, label: l.de || l.en || "", de: l.de, en: l.en }; });
      state.videoExisting = a.video || null;
      if (a.video) { $("#videoKind").value = a.video.kind; $("#videoUrl").value = a.video.kind === "file" ? "" : a.video.url; }
      renderCover(); renderPhotos(); renderLinks(); syncVideo(); show("editor");
    }, function (e) { alert(e.message); });
  }

  function deleteArticle(id) {
    return readJSON("content/articles/" + id + ".json").then(function (r) {
      var jobs = [];
      if (r) {
        var a = r.data, media = [a.cover].concat((a.images || []).map(function (i) { return i.src; })).concat(a.video && a.video.kind === "file" ? [a.video.url] : []);
        media.filter(function (p) { return p && /^content\/media\//.test(p); }).forEach(function (p) { jobs.push(function () { return getFile(p).then(function (f) { return f && delFile(p, f.sha, by("Medien zu Artikel entfernt")); }); }); });
        jobs.push(function () { return delFile("content/articles/" + id + ".json", r.sha, by("Artikel entfernt: " + id)); });
      }
      return jobs.reduce(function (pr, j) { return pr.then(j); }, Promise.resolve());
    }).then(function () { return updateIndex(function (arr) { return arr.filter(function (x) { return x.id !== id; }); }, "Artikelliste aktualisiert"); });
  }
  // Die Reihenfolge in index.json ist die Reihenfolge auf der Website
  function updateIndex(fn, msg) {
    return readJSON(IDX).then(function (r) {
      var arr = fn(r ? (r.data.articles || []) : []);
      return putFile(IDX, b64enc(JSON.stringify({ articles: arr }, null, 1)), by(msg), r && r.sha);
    });
  }
  // neuer Artikel: vor dem ersten älteren einsortieren
  function insertByDate(arr, e) { var i = arr.findIndex(function (x) { return x.date < e.date; }); if (i < 0) arr.push(e); else arr.splice(i, 0, e); return arr; }
  // gespeicherte Reihenfolge anwenden; inzwischen von anderen hinzugefügte Artikel nach Datum einsortieren
  function applyOrder(arr, order) {
    var pos = Object.create(null); order.forEach(function (id, i) { pos[id] = i; });
    var known = arr.filter(function (x) { return x.id in pos; }).sort(function (a, b) { return pos[a.id] - pos[b.id]; });
    arr.filter(function (x) { return !(x.id in pos); }).forEach(function (x) { insertByDate(known, x); });
    return known;
  }

  /* ---------- Übersetzen / Vorschau / Veröffentlichen ---------- */
  function collect() {
    var a = { id: state.id, date: val("date") || today(), category: val("category"), cover: null, images: [], video: null, links: [] };
    ["de", "en"].forEach(function (l) { a[l] = { title: val("title-" + l).trim(), summary: val("summary-" + l).trim(), body: val("body-" + l).trim() }; });
    return a;
  }
  function translateOther(quiet) {
    var from = srcLang(), to = otherLang();
    var src = { title: val("title-" + from).trim(), summary: val("summary-" + from).trim(), body: val("body-" + from).trim() };
    if (!src.title || !src.body) { if (!quiet) alert(t("needTitle")); return Promise.reject(new Error("empty")); }
    $("#trStatus").textContent = t("translating");
    // Überschrift/Kurzfassung/Text + Bildunterschriften + Linkbeschriftungen
    return Promise.all([trShort(src.title, from, to), trShort(src.summary, from, to), trMarkdown(src.body, from, to)]).then(function (r) {
      $("#title-" + to).value = r[0]; $("#summary-" + to).value = r[1]; $("#body-" + to).value = r[2];
      return Promise.all(state.photos.map(function (p) { return p.cap && !p["cap_" + to] ? trShort(p.cap, from, to).then(function (o) { p["cap_" + to] = o; }) : null; })
        .concat(state.links.map(function (l) { return l.label && !l["label_" + to] ? trShort(l.label, from, to).then(function (o) { l["label_" + to] = o; }) : null; })));
    }).then(function () { $("#trStatus").textContent = t("translated"); setTab(to); }, function (e) { $("#trStatus").textContent = t("trFail"); throw e; });
  }
  $("#translateBtn").onclick = function () { translateOther().catch(function () {}); };

  function previewArticle(a, lang) {
    var cover = state.cover ? (state.cover.dataUrl || state.cover.path) : "";
    var p = { id: "preview", date: a.date, category: a.category, cover: cover, de: a.de, en: a.en, images: [], links: [], video: null };
    state.photos.forEach(function (ph) { p.images.push({ src: ph.dataUrl || ph.path, de: capFor(ph, "de"), en: capFor(ph, "en") }); });
    state.links.forEach(function (l) { if (l.url) p.links.push({ url: l.url, de: labelFor(l, "de"), en: labelFor(l, "en") }); });
    var k = val("videoKind"); if (k === "youtube" || k === "vimeo") p.video = { kind: k, url: val("videoUrl").trim() };
    var box = $("#modalBody"); box.innerHTML = UH.renderArticle(p, lang); UH.wireArticle(box);
    $("#pv-de").setAttribute("aria-selected", lang === "de"); $("#pv-en").setAttribute("aria-selected", lang === "en");
    $("#modal").hidden = false;
  }
  function capFor(p, l) { return p["cap_" + l] || (srcLang() === l ? p.cap : "") || (l === "de" ? p.capDe : p.capEn) || p.cap || ""; }
  function labelFor(x, l) { return x["label_" + l] || (srcLang() === l ? x.label : "") || x[l] || x.label || ""; }
  $("#previewBtn").onclick = function () { var a = collect(); previewArticle(a, srcLang()); $("#modal").dataset.cur = srcLang(); };
  $("#pv-de").onclick = function () { previewArticle(collect(), "de"); }; $("#pv-en").onclick = function () { previewArticle(collect(), "en"); };
  $("#closeModal").onclick = function () { $("#modal").hidden = true; };

  function status(msg, cls) { var s = $("#pubStatus"); s.className = cls || "muted"; s.innerHTML = msg; }

  $("#publishBtn").onclick = function () {
    var btn = this, from = srcLang(), to = otherLang();
    if (!val("title-" + from).trim() || !val("body-" + from).trim()) { alert(t("needTitle")); return; }
    btn.disabled = true; status(t("publishing"));
    var needTr = !val("title-" + to).trim() || !val("body-" + to).trim();
    (needTr ? translateOther(true) : Promise.resolve()).catch(function () {
      // Übersetzung fehlgeschlagen: mit Quelltext in beiden Sprachen veröffentlichen, Autor wird informiert
      ["title", "summary", "body"].forEach(function (f) { if (!val(f + "-" + to).trim()) $("#" + f + "-" + to).value = val(f + "-" + from); });
    }).then(publish).then(function (id) {
      status(t("done") + '<a href="' + SITE_URL + "artikel.html?id=" + encodeURIComponent(id) + '" target="_blank" rel="noopener">' + SITE_URL + "artikel.html?id=" + UH.esc(id) + "</a>", "ok");
    }).catch(function (e) { status(UH.esc(e.message || String(e)), "err"); }).then(function () { btn.disabled = false; });
  };

  function publish() {
    var a = collect(), isNew = !state.id;
    a.id = state.id || (a.date + "-" + (slugify(a.de.title || a.en.title) || "artikel"));
    a.author = (state.existing && state.existing.author) || "Redaktion";
    var base = "content/media/" + a.id + "/", n = 0, total = 0;
    function step(label) { n++; status(t("saving") + " (" + n + " " + t("of") + " ~" + total + "): " + label); }

    // Medien vorbereiten
    var uploads = []; // {path, b64}
    function addUpload(path, b64) { uploads.push({ path: path, b64: b64 }); return path; }
    if (state.cover) a.cover = state.cover.dataUrl ? addUpload(base + "cover.jpg", dataUrlB64(state.cover.dataUrl)) : state.cover.path;
    state.photos.forEach(function (p, i) {
      var path = p.dataUrl ? addUpload(base + "foto-" + (i + 1) + "-" + Date.now().toString(36) + ".jpg", dataUrlB64(p.dataUrl)) : p.path;
      a.images.push({ src: path, de: capFor(p, "de"), en: capFor(p, "en") });
    });
    state.links.forEach(function (l) { var u = UH.safeUrl(l.url); if (u) a.links.push({ url: u, de: labelFor(l, "de") || u, en: labelFor(l, "en") || u }); });
    var k = val("videoKind"), videoReady = Promise.resolve();
    if (k === "youtube" || k === "vimeo") { var vu = val("videoUrl").trim(); if (vu) a.video = { kind: k, url: vu }; }
    else if (k === "file") {
      if (state.videoNewFile) {
        var f = state.videoNewFile, ext = (f.name.split(".").pop() || "mp4").toLowerCase().replace(/[^a-z0-9]/g, "");
        videoReady = fileToDataUrl(f).then(function (u) { a.video = { kind: "file", url: addUpload(base + "video." + ext, dataUrlB64(u)) }; });
      } else if (state.videoExisting && state.videoExisting.kind === "file") a.video = state.videoExisting;
    }
    return videoReady.then(function () {
      total = uploads.length + 2;
      // Bilder nacheinander hochladen
      return uploads.reduce(function (pr, u) {
        return pr.then(function () { step(u.path.split("/").pop()); return getFile(u.path).then(function (ex) { return putFile(u.path, u.b64, by("Medien für Artikel " + a.id), ex && ex.sha); }); });
      }, Promise.resolve());
    }).then(function () {
      step("Artikel");
      return getFile("content/articles/" + a.id + ".json").then(function (ex) { return putFile("content/articles/" + a.id + ".json", b64enc(JSON.stringify(a, null, 1)), by((isNew ? "Neuer Artikel: " : "Artikel bearbeitet: ") + a.id), ex && ex.sha); });
    }).then(function () {
      step("Index");
      var entry = { id: a.id, date: a.date, category: a.category, cover: a.cover, de: { title: a.de.title, summary: a.de.summary }, en: { title: a.en.title, summary: a.en.summary } };
      // bearbeiteter Artikel behält seinen Platz; nur bei geändertem Datum wird er neu einsortiert
      return updateIndex(function (arr) {
        var i = arr.findIndex(function (x) { return x.id === a.id; });
        if (i > -1 && arr[i].date === a.date) { arr[i] = entry; return arr; }
        if (i > -1) arr.splice(i, 1);
        return insertByDate(arr, entry);
      }, "Artikelliste aktualisiert");
    }).then(function () { state.id = a.id; return a.id; });
  }

  /* ---------- Anmeldung, Ersteinrichtung, Token-Erneuerung ---------- */
  // Sprungziele von der Website: admin/#edit=<id>, admin/#new
  var jump = location.hash; if (jump) history.replaceState(null, "", location.pathname + location.search);
  function route() {
    var m = jump.match(/^#edit=([a-z0-9-]+)$/), j = jump; jump = "";
    if (m) return openEditor(m[1]);
    if (j === "#new") return newArticle();
    return loadList();
  }
  window.addEventListener("hashchange", function () {
    jump = location.hash; history.replaceState(null, "", location.pathname + location.search);
    if (sess && !$("#list").hidden || sess && !$("#editor").hidden) route();
  });
  function enter() {
    return checkRepo().then(route, function (e) {
      if (e.status === 401 || e.status === 403) {
        if (sess.role === "owner" && sess.mk) { show("renew"); return; }
        sess = null; clearStore(); showLogin(t("tokenExpired")); return;
      }
      throw e;
    });
  }
  function showLogin(msg) { show("login"); $("#loginErr").textContent = msg || ""; }
  function showSetup(exists) {
    show("setup"); $("#setupWarn").hidden = !exists; $("#setupBack").hidden = !exists;
    if (exists && accCache && accCache.users) {
      var u = accCache.users;
      $("#names").value = Object.keys(u).sort(function (a, b) { return (u[b].role === "owner") - (u[a].role === "owner"); }).join(", ");
    }
  }
  function busy(btn, on, label) { btn.disabled = on; btn.textContent = on ? t("working") : t(label); }

  $("#loginForm").onsubmit = function (ev) {
    ev.preventDefault();
    var user = $("#user").value.trim().toLowerCase(), pw = $("#pw").value.trim(), btn = $("#loginBtn");
    $("#loginErr").textContent = ""; busy(btn, true);
    fetchAccounts().then(function (acc) {
      if (!acc) { showSetup(false); return; }
      return unlock(acc, user, pw).then(function (s) { sess = s; remember = $("#remember").checked; storeSess(); $("#pw").value = ""; return enter(); });
    }).catch(function (e) { $("#loginErr").textContent = e.message === "Failed to fetch" ? t("netErr") : e.message; })
      .then(function () { busy(btn, false, "login"); });
  };
  $("#toSetup").onclick = function () { fetchAccounts().then(function (acc) { showSetup(!!acc); }, function () { showSetup(true); }); };
  $("#setupBack").onclick = function () { showLogin(); };

  $("#setupForm").onsubmit = function (ev) {
    ev.preventDefault();
    var tok = $("#token").value.trim(), btn = $("#setupBtn"), names;
    $("#setupErr").textContent = "";
    try { names = parseNames($("#names").value); } catch (e) { $("#setupErr").textContent = e.message; return; }
    busy(btn, true);
    var mkRaw = rand(32), creds = [], acc = {
      v: 1, info: "Zugänge des Autorenpanels. Passwörter sind nicht gespeichert; der GitHub-Token ist verschlüsselt (AES-GCM, Schlüssel pro Login über PBKDF2-SHA-256).",
      vault: null, users: {}
    };
    checkRepo(tok).then(function () { return sealToken(mkRaw, tok); }).then(function (vault) {
      acc.vault = vault;
      return names.reduce(function (pr, n, i) {
        return pr.then(function () {
          var pw = genPassword(); creds.push([n, pw]);
          return wrapFor(pw, mkRaw).then(function (w) { w.role = i ? "editor" : "owner"; w.created = today(); acc.users[n] = w; });
        });
      }, Promise.resolve());
    }).then(function () {
      sess = { user: names[0], role: "owner", token: tok, mk: u8b64(mkRaw) };
      return saveAccounts(function () { return acc; }, "Zugänge für das Autorenpanel eingerichtet");
    }).then(function () {
      accCache = acc; remember = true; storeSess(); $("#token").value = "";
      showCreds(creds, function () { enter(); });
    }).catch(function (e) {
      sess = null; $("#setupErr").textContent = (e.status === 401 || e.status === 404) ? t("bad_token") : e.message;
    }).then(function () { busy(btn, false, "setupBtn"); });
  };

  $("#renewForm").onsubmit = function (ev) {
    ev.preventDefault();
    var tok = $("#renewToken").value.trim(), btn = $("button", this);
    $("#renewErr").textContent = ""; busy(btn, true);
    replaceToken(tok).then(function () { $("#renewToken").value = ""; UH.toast(t("tokenReplaced")); return enter(); },
      function (e) { $("#renewErr").textContent = (e.status === 401 || e.status === 404) ? t("bad_token") : e.message; })
      .then(function () { busy(btn, false, "renewBtn"); });
  };

  $("#logout").onclick = function () { sess = null; accUsers = null; clearStore(); showLogin(); };
  $("#uiLang").onclick = function () { ui = ui === "de" ? "ru" : "de"; localStorage.setItem("uh-admin-ui", ui); applyUi(); };
  $$("[data-eye]").forEach(function (b) { b.onclick = function () { var i = $("#" + b.getAttribute("data-eye")); i.type = i.type === "password" ? "text" : "password"; }; });
  $("#email").value = email;
  $("#email").onchange = function () { email = this.value.trim(); if (email) localStorage.setItem("uh-email", email); else localStorage.removeItem("uh-email"); };
  $("#date").value = today();

  applyUi();
  if (sess && sess.token) enter().catch(function (e) { showLogin(e.message === "Failed to fetch" ? t("netErr") : e.message); });
  else fetchAccounts().then(function (acc) { if (acc) showLogin(); else showSetup(false); }, function () { showLogin(t("netErr")); });
})();
