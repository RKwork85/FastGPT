import { Box, Flex, FlexProps } from '@chakra-ui/react';
import { DatasetTypeEnum } from '@fastgpt/global/core/dataset/constants';
import MyIcon from '@fastgpt/web/components/common/Icon';
import React, { useMemo } from 'react';
import { useTranslation } from 'next-i18next';

const SideTag = ({ type, ...props }: { type: `${DatasetTypeEnum}` } & FlexProps) => {
  if (type === DatasetTypeEnum.folder) return null;
  const { t } = useTranslation();
  const DatasetListTypeMap = useMemo(() => {
    return {
      [DatasetTypeEnum.dataset]: {
        icon: 'core/dataset/commonDatasetOutline',
        label: t('dataset:common_dataset'),
        collectionLabel: 'common.File'
      },
      [DatasetTypeEnum.websiteDataset]: {
        icon: 'core/dataset/websiteDatasetOutline',
        label: t('dataset:website_dataset'),
        collectionLabel: 'common.Website'
      },
      [DatasetTypeEnum.externalFile]: {
        icon: 'core/dataset/externalDatasetOutline',
        label: t('dataset:external_file'),
        collectionLabel: 'common.File'
      }
    };
  }, [t]);
  const item = DatasetListTypeMap[type] || DatasetListTypeMap['dataset'];

  return (
    <Flex
      bg={'myGray.100'}
      borderWidth={'1px'}
      borderColor={'myGray.200'}
      py={'3px'}
      pl={'8px'}
      pr={'12px'}
      borderRadius={'md'}
      fontSize={'xs'}
      alignItems={'center'}
      {...props}
    >
      <MyIcon name={item.icon as any} w={'0.8rem'} color={'myGray.400'} />
      <Box fontSize={'mini'} ml={1}>
        {/* @ts-ignore */}
        {item.label}
      </Box>
    </Flex>
  );
};

export default SideTag;