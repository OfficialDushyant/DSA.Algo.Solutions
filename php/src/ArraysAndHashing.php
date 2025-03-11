<?php
namespace App\Src;

class ArraysAndHashing
{
    public function twoSum(array $nums, int $target): array
    {
        $map = [];
        foreach ($nums as $index => $num) {
            $complete = $target - $num;

            if (isset($map[$complete])) {
                return [$map[$complete], $index];
            }

            $map[$num] = $index;
        }

        return [];
    }

    public function containsDuplicate(array $nums): bool
    {
        $seen = [];
        foreach ($nums as $num) {
            if (isset($seen[$num])) {
                return true;
            }
            $seen[$num] = true;
        }
        return false;
    }

    public function containsDuplicateAlternative(array $nums): bool
    {
        if (count($nums) != count(array_unique($nums))) {
            return true;
        }

        return false;
    }

    public function isAnagram(string $s, string $t): bool
    {
        if (strlen($s) != strlen($t)) {
            return false;
        }

        $char_map = [];

        for ($i = 0; $i < strlen($s); $i++) {
            if (isset($char_map[$s[$i]])) {
                $char_map[$s[$i]]++;
            } else {
                $char_map[$s[$i]] = 1;
            }
        }
        
        for ($i = 0; $i < strlen($t); $i++) {
            if (isset($char_map[$t[$i]]) && $char_map[$t[$i]] > 0) {
                $char_map[$t[$i]]--;
            } else {
                return false;
            }
        }

        return true;
    }

    public function isAnagramAlternative(string $s, string $t): bool
    {
        if (strlen($s) != strlen($t)) {
            return false;
        }

        $char_map = [];

        for ($i = 0; $i < strlen($s); $i++) {
            isset($char_map[$s[$i]]) ? $char_map[$s[$i]]++ : $char_map[$s[$i]] = 1;
            isset($char_map[$t[$i]]) ? $char_map[$t[$i]]-- : $char_map[$t[$i]] = -1;
        }

        foreach ($char_map as $char => $count) {
            if ($count != 0) {
                return false;
            }
        }

        return true;
    }
}
