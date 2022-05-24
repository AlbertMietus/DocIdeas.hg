needs_types = [
    dict(directive="resolution", title="Resolution",     prefix="R_", color="#9DC5BB", style="boundary"),
    dict(directive="use",        title="UseCase",        prefix="U_", color="#C5EBC3", style="usecase"), #Note: usecase does not nest -- needed for :np:
    dict(directive="spec",       title="Specification",  prefix="S_", color="#FEDCD2", style="component"),
    dict(directive="impl",       title="Implementation", prefix="I_", color="#DF744A", style="artifact"),
    dict(directive="verify",     title="Verify",         prefix="V_", color="#F6E27F", style="folder"),
    dict(directive="risk",       title="Jeopardize",     prefix="J_", color="#AA1234", style="queue"),
]

needs_layouts = {
    'clean_collapsed': {'grid': 'simple',
                 'layout': {
                     'head': [
                         '<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>>  <<collapse_button("meta", '
                         'collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=True)>> '],
                     'meta': [
                         '<<meta_all(no_links=True)>>',
                         '<<meta_links_all()>>'],
                 }}}
