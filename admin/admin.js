/* Autorenpanel: schreibt Artikel (JSON + Bilder) per GitHub-API ins Repository.
   Die Website (GitHub Pages) veröffentlicht die Änderung danach automatisch (ca. 1 Minute).
   Der Token bleibt ausschließlich im Browser (localStorage bzw. sessionStorage). */
(function () {
  "use strict";
  var OWNER = "arsencho31", REPO = "stiftung-uni-heidelberg-website", BRANCH = "main";
  var SITE_URL = "https://" + OWNER + ".github.io/" + REPO + "/";
  var API = "https://api.github.com/repos/" + OWNER + "/" + REPO + "/";
  var UH = window.UH;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- Oberfläche: Deutsch / Russisch ---------- */
  var S = {
    de: {
      title: "Autorenpanel", logout: "Abmelden", loginTitle: "Anmelden",
      loginIntro: "Dieses Panel veröffentlicht Artikel direkt im GitHub-Repository der Website. Zum Anmelden brauchen Sie einen persönlichen Zugriffstoken (einmalig erstellen, bleibt nur in Ihrem Browser).",
      tokenLabel: "GitHub-Token", emailLabel: "E-Mail für die Übersetzung (optional – erhöht das kostenlose Tageslimit)", remember: "Auf diesem Gerät angemeldet bleiben", login: "Anmelden",
      articles: "Artikel", newArticle: "+ Neuer Artikel", back: "← Zurück", writeIn: "Ich schreibe auf", category: "Erscheint bei", both: "Beiden", date: "Datum",
      "title-field": "Titel", summary: "Kurzfassung (1–2 Sätze, erscheint auf den Karten)", text: "Text", translate: "Jetzt in die andere Sprache übersetzen",
      media: "Fotos und Video", cover: "Titelbild", photos: "Weitere Fotos (mehrere möglich)", videoKind: "Video", none: "Kein Video", videoFile: "Eigene Videodatei (MP4, bis 40 MB)",
      videoUrl: "Link zum Video", videoPick: "MP4-Datei", linksH: "Links", addLink: "+ Link hinzufügen", preview: "Vorschau", publish: "Veröffentlichen (DE + EN)", close: "Schließen",
      howTitle: "So erstellen Sie den Token (2 Minuten)",
      // dynamisch
      bad_token: "Token ungültig oder ohne Schreibrecht für dieses Repository.", edit: "Bearbeiten", del: "Löschen", view: "Ansehen", editTitle: "Artikel bearbeiten", noArticles: "Noch keine Artikel.",
      confirmDel: "Diesen Artikel wirklich löschen? (Dauerhaft entfernt.)", needTitle: "Bitte Titel und Text in der gewählten Sprache eingeben.", translating: "Übersetze …", translated: "Übersetzung eingefügt – bitte kurz prüfen.",
      trFail: "Automatische Übersetzung nicht möglich (Limit erreicht oder offline). Bitte Text im anderen Tab selbst eintragen.", trHintSrc: "Sie schreiben auf {l}. Der andere Tab wird beim Veröffentlichen automatisch übersetzt.",
      publishing: "Veröffentliche …", done: "Veröffentlicht! Sichtbar nach ca. 1 Minute: ", remove: "Entfernen", caption: "Bildunterschrift", linkLabel: "Beschriftung", linkUrl: "Adresse (https://…)", tooBig: "Datei zu groß (max. 40 MB).",
      keep: "Aktuelles Video bleibt erhalten, falls Sie nichts Neues wählen.", loaded: "Angemeldet", saving: "Speichere", of: "von"
    },
    ru: {
      title: "Панель автора", logout: "Выйти", loginTitle: "Вход",
      loginIntro: "Панель публикует статьи прямо в GitHub-репозиторий сайта. Для входа нужен личный токен доступа (создаётся один раз и хранится только в вашем браузере).",
      tokenLabel: "GitHub-токен", emailLabel: "E-mail для перевода (необязательно — увеличивает бесплатный дневной лимит)", remember: "Оставаться в системе на этом устройстве", login: "Войти",
      articles: "Статьи", newArticle: "+ Новая статья", back: "← Назад", writeIn: "Пишу на языке", category: "Показывать у", both: "Обоих", date: "Дата",
      "title-field": "Заголовок", summary: "Краткое описание (1–2 предложения, для карточек)", text: "Текст", translate: "Перевести сейчас на другой язык",
      media: "Фото и видео", cover: "Главное фото", photos: "Дополнительные фото (можно несколько)", videoKind: "Видео", none: "Без видео", videoFile: "Свой видеофайл (MP4, до 40 МБ)",
      videoUrl: "Ссылка на видео", videoPick: "Файл MP4", linksH: "Ссылки", addLink: "+ Добавить ссылку", preview: "Предпросмотр", publish: "Опубликовать (DE + EN)", close: "Закрыть",
      howTitle: "Как создать токен (2 минуты)",
      bad_token: "Токен недействителен или нет права записи в этот репозиторий.", edit: "Изменить", del: "Удалить", view: "Открыть", editTitle: "Редактирование статьи", noArticles: "Статей пока нет.",
      confirmDel: "Удалить статью насовсем?", needTitle: "Введите заголовок и текст на выбранном языке.", translating: "Перевожу …", translated: "Перевод вставлен — коротко проверьте.",
      trFail: "Автоперевод недоступен (лимит или нет сети). Заполните второй язык вручную.", trHintSrc: "Вы пишете на языке: {l}. Вторая вкладка переведётся автоматически при публикации.",
      publishing: "Публикую …", done: "Опубликовано! Появится на сайте примерно через минуту: ", remove: "Убрать", caption: "Подпись к фото", linkLabel: "Название", linkUrl: "Адрес (https://…)", tooBig: "Файл слишком большой (макс. 40 МБ).",
      keep: "Текущее видео сохранится, если не выбрать новое.", loaded: "Вход выполнен", saving: "Сохраняю", of: "из"
    }
  };
  var HTMLK = {
    de: {
      how1: 'Öffnen Sie <a href="https://github.com/settings/personal-access-tokens/new" target="_blank" rel="noopener">github.com/settings/personal-access-tokens/new</a> (bei GitHub angemeldet).',
      how2: '„Repository access“: <b>Only select repositories</b> → <code>stiftung-uni-heidelberg-website</code> wählen.',
      how3: '„Permissions“ → „Repository permissions“ → <b>Contents: Read and write</b>.',
      how4: '„Generate token“ klicken und den Token (beginnt mit <code>github_pat_</code>) hier einfügen.',
      how5: 'Weitere Redakteur:innen: unter GitHub → Repository → Settings → Collaborators einladen; jede Person erstellt ihren eigenen Token.',
      mdHelp: 'Formatierung: <code>## Zwischenüberschrift</code>, <code>- Listenpunkt</code>, <code>**fett**</code>, <code>*kursiv*</code>, <code>[Linktext](https://…)</code>. Leerzeile = neuer Absatz.'
    },
    ru: {
      how1: 'Откройте <a href="https://github.com/settings/personal-access-tokens/new" target="_blank" rel="noopener">github.com/settings/personal-access-tokens/new</a> (войдя в GitHub).',
      how2: '«Repository access»: <b>Only select repositories</b> → выберите <code>stiftung-uni-heidelberg-website</code>.',
      how3: '«Permissions» → «Repository permissions» → <b>Contents: Read and write</b>.',
      how4: 'Нажмите «Generate token» и вставьте токен (начинается с <code>github_pat_</code>) сюда.',
      how5: 'Другие редакторы: пригласите их в GitHub → репозиторий → Settings → Collaborators; у каждого свой токен.',
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
  }

  /* ---------- Token / GitHub-API ---------- */
  var token = sessionStorage.getItem("uh-token") || localStorage.getItem("uh-token") || "";
  var email = localStorage.getItem("uh-email") || "";
  function headers(extra) { return Object.assign({ Authorization: "Bearer " + token, Accept: "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28" }, extra || {}); }
  function gh(path, opts) {
    opts = opts || {}; opts.headers = headers(opts.headers);
    return fetch(API + path, opts).then(function (r) {
      if (r.status === 404 && opts.allow404) return null;
      if (!r.ok) return r.json().catch(function () { return {}; }).then(function (j) { var e = new Error(j.message || r.status); e.status = r.status; throw e; });
      return r.status === 204 ? {} : r.json();
    });
  }
  function b64enc(str) { var b = new TextEncoder().encode(str), s = ""; b.forEach(function (c) { s += String.fromCharCode(c); }); return btoa(s); }
  function b64dec(b64) { var s = atob(b64.replace(/\n/g, "")), a = new Uint8Array(s.length); for (var i = 0; i < s.length; i++) a[i] = s.charCodeAt(i); return new TextDecoder().decode(a); }
  function getFile(path) { return gh("contents/" + path.split("/").map(encodeURIComponent).join("/") + "?ref=" + BRANCH, { allow404: true }); }
  function putFile(path, b64, msg, sha) {
    var body = { message: msg, content: b64, branch: BRANCH }; if (sha) body.sha = sha;
    return gh("contents/" + path.split("/").map(encodeURIComponent).join("/"), { method: "PUT", body: JSON.stringify(body) });
  }
  function delFile(path, sha, msg) { return gh("contents/" + path.split("/").map(encodeURIComponent).join("/"), { method: "DELETE", body: JSON.stringify({ message: msg, sha: sha, branch: BRANCH }) }); }
  function readJSON(path) { return getFile(path).then(function (f) { return f ? { sha: f.sha, data: JSON.parse(b64dec(f.content)) } : null; }); }

  /* ---------- Hilfsfunktionen ---------- */
  function show(id) { ["login", "list", "editor"].forEach(function (s) { $("#" + s).hidden = s !== id; }); $("#logout").hidden = id === "login"; window.scrollTo(0, 0); }
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

  /* ---------- Übersetzung (MyMemory, kostenlos, ohne Schlüssel) ---------- */
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

  /* ---------- Artikelliste ---------- */
  function loadList() {
    show("list"); $("#repoInfo").textContent = OWNER + "/" + REPO; $("#rows").innerHTML = "…";
    return readJSON("content/articles/index.json").then(function (r) {
      var list = r ? (r.data.articles || []) : [];
      $("#rows").innerHTML = list.length ? "" : '<p class="empty">' + t("noArticles") + "</p>";
      list.forEach(function (a) {
        var row = document.createElement("div"); row.className = "art-row";
        var ti = (a.de && a.de.title) || (a.en && a.en.title) || a.id;
        row.innerHTML = '<div><b>' + UH.esc(ti) + '</b><span class="meta">' + UH.esc(a.date) + " · " + UH.esc(a.category) + '</span></div><div class="btns"><a class="btn ghost sm" target="_blank" rel="noopener" href="' + SITE_URL + "artikel.html?id=" + encodeURIComponent(a.id) + '">' + t("view") + '</a><button class="btn sm" type="button" data-e>' + t("edit") + '</button><button class="btn danger sm" type="button" data-d>' + t("del") + "</button></div>";
        $("[data-e]", row).onclick = function () { openEditor(a.id); };
        $("[data-d]", row).onclick = function () { if (confirm(t("confirmDel"))) deleteArticle(a.id).then(loadList, function (e) { alert(e.message); }); };
        $("#rows").appendChild(row);
      });
    }, function (e) { $("#rows").innerHTML = '<p class="err">' + UH.esc(e.message) + "</p>"; });
  }
  $("#newBtn").onclick = function () { resetEditor(); $("#edTitle").textContent = t("newArticle"); show("editor"); };
  $("#cancelBtn").onclick = loadList;

  function openEditor(id) {
    readJSON("content/articles/" + id + ".json").then(function (r) {
      if (!r) return; var a = r.data; resetEditor(); state.id = a.id; state.sha = r.sha; state.existing = a;
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
        media.filter(function (p) { return p && /^content\/media\//.test(p); }).forEach(function (p) { jobs.push(function () { return getFile(p).then(function (f) { return f && delFile(p, f.sha, "Medien zu Artikel entfernt"); }); }); });
        jobs.push(function () { return delFile("content/articles/" + id + ".json", r.sha, "Artikel entfernt: " + id); });
      }
      return jobs.reduce(function (pr, j) { return pr.then(j); }, Promise.resolve());
    }).then(function () { return updateIndex(function (arr) { return arr.filter(function (x) { return x.id !== id; }); }, "Artikelliste aktualisiert"); });
  }
  function updateIndex(fn, msg) {
    return readJSON("content/articles/index.json").then(function (r) {
      var arr = fn(r ? (r.data.articles || []) : []).sort(function (a, b) { return a.date < b.date ? 1 : -1; });
      return putFile("content/articles/index.json", b64enc(JSON.stringify({ articles: arr }, null, 1)), msg, r && r.sha);
    });
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
    var base = "content/media/" + a.id + "/", jobs = [], n = 0, total = 0;
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
        return pr.then(function () { step(u.path.split("/").pop()); return getFile(u.path).then(function (ex) { return putFile(u.path, u.b64, "Medien für Artikel " + a.id, ex && ex.sha); }); });
      }, Promise.resolve());
    }).then(function () {
      step("Artikel");
      return getFile("content/articles/" + a.id + ".json").then(function (ex) { return putFile("content/articles/" + a.id + ".json", b64enc(JSON.stringify(a, null, 1)), (isNew ? "Neuer Artikel: " : "Artikel bearbeitet: ") + a.id, ex && ex.sha); });
    }).then(function () {
      step("Index");
      var entry = { id: a.id, date: a.date, category: a.category, cover: a.cover, de: { title: a.de.title, summary: a.de.summary }, en: { title: a.en.title, summary: a.en.summary } };
      return updateIndex(function (arr) { return arr.filter(function (x) { return x.id !== a.id; }).concat(entry); }, "Artikelliste aktualisiert");
    }).then(function () { state.id = a.id; return a.id; });
  }

  /* ---------- Anmeldung ---------- */
  function enter() {
    return gh("", {}).then(function (repo) {
      if (!repo.permissions || !repo.permissions.push) throw new Error(t("bad_token"));
      loadList();
    });
  }
  $("#loginForm").onsubmit = function (ev) {
    ev.preventDefault(); token = $("#token").value.trim(); email = $("#email").value.trim(); $("#loginErr").textContent = "";
    enter().then(function () {
      var store = $("#remember").checked ? localStorage : sessionStorage; store.setItem("uh-token", token);
      if (email) localStorage.setItem("uh-email", email); $("#token").value = "";
    }, function (e) { token = ""; $("#loginErr").textContent = (e.status === 401 || e.status === 404) ? t("bad_token") : e.message; });
  };
  $("#logout").onclick = function () { localStorage.removeItem("uh-token"); sessionStorage.removeItem("uh-token"); token = ""; show("login"); };
  $("#uiLang").onclick = function () { ui = ui === "de" ? "ru" : "de"; localStorage.setItem("uh-admin-ui", ui); applyUi(); };

  $("#email").value = email; $("#date").value = today();
  applyUi();
  if (token) enter().catch(function () { token = ""; localStorage.removeItem("uh-token"); sessionStorage.removeItem("uh-token"); show("login"); }); else show("login");
})();
