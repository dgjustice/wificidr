package bintree

import "testing"

func TestNewNode(t *testing.T) {
	n := NewNode(1, "", nil, nil)
	if n.left != nil && n.right != nil {
		t.Error("Left and Right should be nil")
	}
}
