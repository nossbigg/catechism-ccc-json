def validate_has_all_ccc_refs(page_nodes_dict):
    ccc_refs = {}

    for page in page_nodes_dict.values():
        for paragraph in page.paragraphs:
            for element in paragraph.elements:
                if element['type'] == 'ref-ccc':
                    ccc_refs[element['ref_number']] = ''

    expected_num_ccc_refs = 2865
    missing_refs = []

    for i in range(1, expected_num_ccc_refs):
        if i not in ccc_refs:
            missing_refs.append(i)

    return len(missing_refs) == 0
