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

func NewNode(subnet uint, flag string, left *node, right *node) (*node) {
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

// func AllocateNode(root *node, prefixlen uint) *node {
//     if root.subnet.prefixlen >= prefixlen {
//         if root.flag == "A" {
//             return nil
// 		} else if root.flag == "F" {
//             root.flag = "A"
//             return root
// 		}
// 	}
//     if root.flag == "F" {
//         splitNode(root)
// 	}
//     if root.left != nil && root.right != nil {
//         return AllocateNode(root.left, prefixlen) | AllocateNode(root.right, prefixlen)
// 	}
// }

func PtoNetUint(netstr string) (uint, error) {
	ip, _, err := net.ParseCIDR(netstr)
	if err != nil {
		return 0, errors.New("invalid IP address")
	}
	if len(ip) == 4 {
		return uint(binary.BigEndian.Uint32(ip)), nil
	} else if len(ip) == 16 {
		return uint(binary.BigEndian.Uint64(ip)), nil
	} else {
		return 0, errors.New("byte array must be len 4 or 16")
	}
}
