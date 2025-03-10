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

    public function containsDuplicate(array $nums): bool{
        $seen = [];
        foreach ($nums as $num){
            if(isset($seen[$num])){
                return true;
            }
            $seen[$num] = true;
        }
        return false;
    }

    public function containsDuplicateAlternative (array $nums): bool
    {
        if(count($nums) != count(array_unique($nums))) {
            return true;
        }

        return false;
    }   
}
