from xml.etree import ElementTree


def element_tree_to_dict(element_tree: ElementTree) -> dict:
    if len(element_tree) == 0:
        text = element_tree.text
        if not text:
            text = ''
        return {element_tree.tag: text}
    else:
        return {
            element_tree.tag: [element_tree_to_dict(child) for child in element_tree]
        }
