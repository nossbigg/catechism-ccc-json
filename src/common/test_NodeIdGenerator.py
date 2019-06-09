from NodeIdGenerator import NodeIdGenerator


def test_generates_ids():
    id_generator = NodeIdGenerator('prefix')
    assert id_generator.generate_id() == 'prefix-1'
    assert id_generator.generate_id() == 'prefix-2'
