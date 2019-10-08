package bintree

import "testing"

func TestNewNode(t *testing.T) {
	t = NewNode(1)
	if t.left != nil && t.right != nil {
		t.Error("Left and Right should be nil")
	}
}
