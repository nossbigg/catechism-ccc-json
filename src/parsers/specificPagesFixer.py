def fixSpecificPagesHtml(pages_dict):
    with_fixed_pages = {}

    for page_toc_ref, page_html in pages_dict.items():
        if page_toc_ref not in pages_to_fix:
            with_fixed_pages[page_toc_ref] = page_html
            continue

        fixer_function = pages_to_fix[page_toc_ref]
        with_fixed_pages[page_toc_ref] = fixer_function(page_html)

    return with_fixed_pages


def fix_for_ref_2077(page_html):
    # Fix for
    # PART THREE: LIFE IN CHRIST
    # SECTION TWO THE TEN COMMANDMENTS
    # IN BRIEF
    # http://www.vatican.va/archive/ENG0015/__P79.HTM
    p = page_html

    # Fix Ref 2077 weird order
    p = p.replace("2076 By his life and by his\n"
                  "preaching Jesus attested to the permanent validity of the Decalogue. 2077 The",
                  "2076 By his life and by his\n"
                  "preaching Jesus attested to the permanent validity of the Decalogue.")
    p = p.replace("gift of the Decalogue is bestowed from within\n"
                  "the covenant concluded by God with his people. God's",
                  "2077 The gift of the Decalogue is bestowed from within\n"
                  "the covenant concluded by God with his people. God's")

    return p


def fix_for_ref_2436(page_html):
    # Fix for
    # PART THREE: LIFE IN CHRIST
    # SECTION TWO THE TEN COMMANDMENTS
    # CHAPTER TWO YOU SHALL LOVE YOUR NEIGHBOR AS YOURSELF
    # Article 7 THE SEVENTH COMMANDMENT
    # IV. Economic Activity and Social Justice
    # http://www.vatican.va/archive/ENG0015/__P8D.HTM
    p = page_html

    # Move Ref 2436 into its own paragraph
    p = p.replace("Recourse to a strike is morally legitimate when it cannot be avoided, or at\n"
                  "least when it is necessary to obtain a proportionate benefit. It becomes\n"
                  "morally unacceptable when accompanied by violence, or when objectives are\n"
                  "included that are not directly linked to working conditions or are contrary to\n"
                  "the common good. <br>\n2436 ",
                  "Recourse to a strike is morally legitimate when it cannot be avoided, or at\n"
                  "least when it is necessary to obtain a proportionate benefit. It becomes\n"
                  "morally unacceptable when accompanied by violence, or when objectives are\n"
                  "included that are not directly linked to working conditions or are contrary to\n"
                  "the common good.</p>\n\n"
                  "<p class=MsoNormal>2436\n")

    return p


pages_to_fix = {
    'toc-279': fix_for_ref_2077,
    'toc-319': fix_for_ref_2436
}
