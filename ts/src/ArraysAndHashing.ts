export default class ArrayAndHashing{
    twoSum(nums: number[], target: number): number[] {
        let map = new Map<number, number>();
        for (let i = 0; i < nums.length; i++) 
            {
            let diff = target - nums[i];
            if (map.has(diff)) {
                return [map.get(diff)!, i];
            }
            map.set(nums[i], i);
        }
        return [];
    }

    containsDuplicate(nums: number[]): boolean {
        const seen = new Set<number>();
        for(let i = 0; i < nums.length; i++){
            if(seen.has(nums[i]))  { 
                return true; 
            }
            seen.add(nums[i]);
        }
        return false;
    }

    containsDuplicateAlternative(nums: number[]): boolean {
        const newNumsSet = new Set(nums);
        return newNumsSet.size !== nums.length;

    }
}