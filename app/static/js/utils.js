class Links {
    #srcList;
    constructor(required_source = []) {
        this.#srcList = new LinkSources();
        if (!Array.isArray(required_source) || !required_source.length) {
            required_source = [],
            console.error('Object is not type of array, or is empty!');
        }

        document.addEventListener('DOMContentLoaded', () => {
            for (const src of required_source) {
                const link = this.#createLink(this.#srcList.getSource(src), "stylesheet");
                if (link) {
                    const element = document.createElement('link');
                    if (link.rel) element.rel = link.rel;
                    element.href = link.href;
                    document.head.appendChild(element);
                }
            }
        });
    }

    #createLink(src, type="") {
        if (typeof(src) === 'undefined') return null;
        const link = { href: src, rel: type || undefined };
        return link;
    }
}

class LinkSources {
    #sourceList = {
        main: 'static/css/main.css',
        index: 'static/css/index.css',
    }

    getSource(key) {
        return this.#sourceList[key];
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.body.style.visibility = 'visible';
});