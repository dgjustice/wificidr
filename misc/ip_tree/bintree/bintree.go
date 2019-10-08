package bintree

import (
	"encoding/binary"
	"net"
	"errors"
)

type node struct {
    subnet uint
    flag string
    left *node
    right *node
}

func NewNode(netstr string, flag string, left *node, right *node) (*node, error) {
	ip, subnet, err := net.ParseCIDR(netstr)
	if err != nil {
		return nil, errors.New("invalid IP address")
	}
	n := &node{
		subnet: subnet,
		flag: flag,
		left: left,
		right: right,
	}
	return n, nil
}

func splitNode(node *node) {
	node.left, err := NewNode(node.subnet << 1, "F", nil, nil)
	node.right, err = NewNode(node.subnet << 1 + 1, "F", nil, nil)
	if node.flag == "F" {
		node.flag = ""
	}
}

func AllocateNode(root *node, prefixlen uint) *node {
    if root.subnet.prefixlen >= prefixlen {
        if root.flag == "A" {
            return nil
		} else if root.flag == "F" {
            root.flag = "A"
            return root
		}
	}
    if root.flag == "F" {
        splitNode(root)
	}
    if root.left != nil && root.right != nil {
        return allocate_node(root.left, prefixlen) | allocate_node(root.right, prefixlen)
	}
}

func IPAddressToUint(bytes [4]byte) uint {
	if len(bytes) == 4 {
		return binary.BigEndian.Uint32(bytes)
	} else if len(bytes) == 16 {
		return binary.BigEndian.Uint64(bytes)
	} else {
		return errors.New("byte array must be len 4 or 16")
	}
}
