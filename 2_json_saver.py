import json

images = [

    {
        'id': 'opo1622d',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo1622d.jpg',
    },

    {
        'id': 'opo1419c',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo1419c.jpg',
    },

    {
        'id': 'opo9736e',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9736e.jpg',
    },

    {
        'id': 'opo9537c',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9537c.jpg',
    },

    {
        'id': 'opo9537b',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9537b.jpg',
    },

    {
        'id': 'opo9535b',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9535b.jpg',
    },

    {
        'id': 'opo9535c',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9535c.jpg',
    },

    {
        'id': 'opo9536a',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9536a.jpg',
    },

    {
        'id': 'opo9518b',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9518b.jpg',
    },

    {
        'id': 'opo9516i',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9516i.jpg',
    },

    {
        'id': 'opo9426b',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9426b.jpg',
    },

    {
        'id': 'opo9426a',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9426a.jpg',
    },

    {
        'id': 'heic2013b',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/heic2013b.jpg',
    },

    {
        'id': 'heic2013c',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/heic2013c.jpg',
    },

    {
        'id': 'heic1715c',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/heic1715c.jpg',
    },

    {
        'id': 'opo9834e',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9834e.jpg',
    },

    {
        'id': 'opo9634i',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9634i.jpg',
    },

    {
        'id': 'opo9634h',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9634h.jpg',
    },

    {
        'id': 'opo9634a3',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9634a3.jpg',
    },

    {
        'id': 'opo9634e',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9634e.jpg',
    },

    {
        'id': 'opo9634d',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9634d.jpg',
    },

    {
        'id': 'opo9634g',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9634g.jpg',
    },

    {
        'id': 'opo9634b',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9634b.jpg',
    },

    {
        'id': 'opo9634c',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9634c.jpg',
    },

    {
        'id': 'opo9634f',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9634f.jpg',
    },

    {
        'id': 'opo9633b',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9633b.jpg',
    },

    {
        'id': 'opo9632b',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9632b.jpg',
    },

    {
        'id': 'opo9632c',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9632c.jpg',
    },

    {
        'id': 'opo1509a',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo1509a.jpg',
    },

    {
        'id': 'heic1010c',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/heic1010c.jpg',
    },

    {
        'id': 'opo9715c2',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9715c2.jpg',
    },

    {
        'id': 'opo9715c3',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9715c3.jpg',
    },

    {
        'id': 'opo9715c1',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9715c1.jpg',
    },

    {
        'id': 'opo9715c4',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9715c4.jpg',
    },

    {
        'id': 'heic2113e',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/heic2113e.jpg',
    },

    {
        'id': 'heic2113d',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/heic2113d.jpg',
    },

    {
        'id': 'heic2113c',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/heic2113c.jpg',
    },

    {
        'id': 'heic1405c',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/heic1405c.jpg',
    },

    {
        'id': 'heic1405b',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/heic1405b.jpg',
    },

    {
        'id': 'heic1320b',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/heic1320b.jpg',
    },

    {
        'id': 'opo1330c',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo1330c.jpg',
    },

    {
        'id': 'opo1330b',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo1330b.jpg',
    },

    {
        'id': 'heic0909a',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/heic0909a.jpg',
    },

    {
        'id': 'opo0405d',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo0405d.jpg',
    },

    {
        'id': 'opo9929a',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9929a.jpg',
    },

    {
        'id': 'opo9834b',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9834b.jpg',
    },

    {
        'id': 'opo9709a',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9709a.jpg',
    },

    {
        'id': 'opo9709b1',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9709b1.jpg',
    },

    {
        'id': 'opo9709b2',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9709b2.jpg',
    },

    {
        'id': 'opo9541a',
        'src': 'https://cdn.spacetelescope.org/archives/images/large/opo9541a.jpg',
    },

]

with open("image_data.json", "w") as json_file:
    json.dump(images, json_file, indent=4)
