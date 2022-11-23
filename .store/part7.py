

new MutationObserver(function() {
    walk(document.body);
}).observe(document.body, {
    childList: true
});'''

            with open(fulldir9, 'w', encoding='utf-8') as f:
                f.write(title + '\n' + endmatch + '\n' + head + '\n\n\t' + zong + '\n\t' + end)