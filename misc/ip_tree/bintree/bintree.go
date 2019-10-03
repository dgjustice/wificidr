package buintree

type node struct {
    subnet uint
    flag string
    left *node
    right *node
}

func NewNode(subnet uint, flag string, left *node, right *node) *node {
	n := &node{
		subnet: subnet,
		flag: flag,
		left: left,
		right: right,
	}
	return n
}

func splitNode(node *node) {
	node.left = NewNode(node.subnet << 1, "F", nil, nil)
	node.right = NewNode(node.subnet << 1 + 1, "F", nil, nil)
	if node.flag == "F" {
		node.flag = ""
	}
}

func AllocateNode(root *node, prefixlen uint) *node {
    if root.subnet.prefixlen >= prefixlen {
        if root.attr == "allocated" {
            return nil
		}
		else if root.attr == "free" {
            root.attr = "allocated"
            return root
		}
	}
    if root.attr == "free" {
        splitNode(root)
	}
    if root.left != nil && root.right != nil {
        return allocate_node(root.left, prefixlen) | allocate_node(root.right, prefixlen)
	}
}
